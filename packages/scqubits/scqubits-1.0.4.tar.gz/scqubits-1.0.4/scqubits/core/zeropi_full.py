# zeropi_full.py
#
# This file is part of scqubits.
#
#    Copyright (c) 2019, Jens Koch and Peter Groszkowski
#    All rights reserved.
#
#    This source code is licensed under the BSD-style license found in the
#    LICENSE file in the root directory of this source tree.
############################################################################

import numpy as np
from scipy import sparse

import scqubits.core.operators as op
from scqubits.core.qubit_base import QubitBaseClass
from scqubits.core.zeropi import ZeroPi
from scqubits.utils.spectrum_utils import order_eigensystem, get_matrixelement_table


class FullZeroPi(QubitBaseClass):
    r"""Zero-Pi qubit [Brooks2013]_ [Dempster2014]_ including coupling to the zeta mode. The circuit is described by the
    Hamiltonian :math:`H = H_{0-\pi} + H_\text{int} + H_\zeta`, where

    .. math::

        &H_{0-\pi} = -2E_\text{CJ}\partial_\phi^2+2E_{\text{C}\Sigma}(i\partial_\theta-n_g)^2
                     +2E_{C\Sigma}dC_J\,\partial_\phi\partial_\theta\\
        &\qquad\qquad\qquad+2E_{C\Sigma}(\delta C_J/C_J)\partial_\phi\partial_\theta
                     +2\,\delta E_J \sin\theta\sin(\phi-\phi_\text{ext}/2)\\
        &H_\text{int} = 2E_{C\Sigma}dC\,\partial_\theta\partial_\zeta + E_L dE_L \phi\,\zeta\\
        &H_\zeta = \omega_\zeta a^\dagger a

    expressed in phase basis. The definition of the relevant charging energies :math:`E_\text{CJ}`,
    :math:`E_{\text{C}\Sigma}`,     Josephson energies :math:`E_\text{J}`, inductive energies :math:`E_\text{L}`,
    and relative amounts of disorder :math:`dC_\text{J}`, :math:`dE_\text{J}`, :math:`dC`, :math:`dE_\text{L}`
    follows [Groszkowski2018]_. Internally, the ``FullZeroPi`` class formulates the Hamiltonian matrix via the
    product basis of the decoupled Zero-Pi qubit (see ``ZeroPi``)  on one hand, and the zeta LC oscillator on the other
    hand.


    Parameters
    ----------
    EJ: float
        mean Josephson energy of the two junctions
    EL: float
        inductive energy of the two (super-)inductors
    ECJ: float
        charging energy associated with the two junctions
    EC: float or None
        charging energy of the large shunting capacitances; set to `None` if `ECS` is provided instead
    dEJ: float
        relative disorder in EJ, i.e., (EJ1-EJ2)/EJavg
    dEL: float
        relative disorder in EL, i.e., (EL1-EL2)/EL(mean)
    dCJ: float
        relative disorder of the junction capacitances, i.e., (CJ1-CJ2)/CJavg
    dC: float
        relative disorder in large capacitances, i.e., (C1-C2)/Cavg
    ng: float
        offset charge associated with theta
    zeropi_cutoff: int
        cutoff in the number of states of the disordered zero-pi qubit
    zeta_cutoff: int
        cutoff in the zeta oscillator basis (Fock state basis)
    flux: float
        magnetic flux through the circuit loop, measured in units of flux quanta (h/2e)
    grid: Grid1d object
        specifies the range and spacing of the discretization lattice
    ncut: int
        charge number cutoff for `n_theta`,  `n_theta = -ncut, ..., ncut`
    ECS: float, optional
        total charging energy including large shunting capacitances and junction capacitances; may be provided instead
        of EC
    truncated_dim: int, optional
        desired dimension of the truncated quantum system
    """

    def __init__(self, EJ, EL, ECJ, EC, dEJ, dCJ, dC, dEL, flux, ng, zeropi_cutoff, zeta_cutoff, grid, ncut,
                 ECS=None, truncated_dim=None):
        self.EJ = EJ
        self.EL = EL
        self.ECJ = ECJ

        if EC is None and ECS is None:
            raise ValueError("Argument missing: must either provide EC or ECS")
        if EC and ECS:
            raise ValueError("Argument error: can only provide either EC or ECS")
        if EC:
            self.EC = EC
        else:
            self.EC = 1 / (1 / ECS - 1 / self.ECJ)

        self.dEJ = dEJ
        self.dCJ = dCJ
        self.dC = dC
        self.dEL = dEL
        self.flux = flux
        self.ng = ng
        self.zeta_cutoff = zeta_cutoff
        self.zeropi_cutoff = zeropi_cutoff
        self.grid = grid
        self.ncut = ncut
        self.truncated_dim = truncated_dim
        self._sys_type = 'full 0-Pi circuit (phi, theta, zeta) in 0pi - zeta product basis'
        self._evec_dtype = np.complex_

        self._zeropi = ZeroPi(
            EJ=self.EJ,
            EL=self.EL,
            ECJ=self.ECJ,
            EC=self.EC,
            dEJ=self.dEJ,
            dCJ=self.dCJ,
            flux=self.flux,
            ng=self.ng,
            grid=self.grid,
            ncut=self.ncut,
            truncated_dim=self.zeropi_cutoff
        )

    def ECS(self):
        """Helper function to calculate and return `ECS`"""
        return 1 / (1 / self.EC + 1 / self.ECJ)

    def set_EC_via_ECS(self, ECS):
        """Helper function to set `EC` by providing `ECS`, keeping `ECJ` constant."""
        self.EC = 1 / (1 / ECS - 1 / self.ECJ)

    def omega_zeta(self):
        """Returns (angular) frequency of the zeta mode"""
        return (8.0 * self.EL * self.EC) ** 0.5

    def hamiltonian(self, return_parts=False):
        """Returns Hamiltonian in basis obtained by discretizing phi, employing charge basis for theta, and Fock
        basis for zeta.

        Parameters
        ----------
        return_parts: bool, optional
            If set to true, `hamiltonian` returns [hamiltonian, evals, evecs, g_coupling_matrix]

        Returns
        -------
        scipy.sparse.csc_matrix or list
        """
        zeropi_dim = self.zeropi_cutoff
        zeropi_evals, zeropi_evecs = self._zeropi.eigensys(evals_count=zeropi_dim)
        zeropi_diag_hamiltonian = sparse.dia_matrix((zeropi_dim, zeropi_dim), dtype=np.complex_)
        zeropi_diag_hamiltonian.setdiag(zeropi_evals)

        zeta_dim = self.zeta_cutoff
        prefactor = self.omega_zeta()
        zeta_diag_hamiltonian = op.number_sparse(zeta_dim, prefactor)

        hamiltonian_mat =  sparse.kron(zeropi_diag_hamiltonian,
                                       sparse.identity(zeta_dim, format='dia', dtype=np.complex_))
        hamiltonian_mat += sparse.kron(sparse.identity(zeropi_dim, format='dia', dtype=np.complex_),
                                       zeta_diag_hamiltonian)

        gmat = self.g_coupling_matrix(zeropi_evecs)
        zeropi_coupling = sparse.dia_matrix((zeropi_dim, zeropi_dim), dtype=np.complex_)
        for l1 in range(zeropi_dim):
            for l2 in range(zeropi_dim):
                zeropi_coupling += gmat[l1, l2] * op.hubbard_sparse(l1, l2, zeropi_dim)
        hamiltonian_mat += sparse.kron(zeropi_coupling,
                                       op.annihilation_sparse(zeta_dim) + op.creation_sparse(zeta_dim))

        if return_parts:
            return [hamiltonian_mat.tocsc(), zeropi_evals, zeropi_evecs, gmat]
        return hamiltonian_mat.tocsc()

    def _zeropi_operator_in_product_basis(self, zeropi_operator, zeropi_evecs=None):
        """Helper method that converts a zeropi operator into one in the product basis'

        TODO: Could update d_hamiltonian_EJ(),  d_hamiltonian_ng(),  d_hamiltonian_flux() to use this.
        """
        zeropi_dim = self.zeropi_cutoff
        zeta_dim = self.zeta_cutoff

        if zeropi_evecs is None:
            _, zeropi_evecs = self._zeropi.eigensys(evals_count=zeropi_dim)

        op_eigen_basis = sparse.dia_matrix((zeropi_dim, zeropi_dim),
                                           dtype=np.complex_)  # is this guaranteed to be zero?

        op_zeropi = get_matrixelement_table(zeropi_operator, zeropi_evecs, real_valued=False)
        for n in range(zeropi_dim):
            for m in range(zeropi_dim):
                op_eigen_basis += op_zeropi[n, m] * op.hubbard_sparse(n, m, zeropi_dim)

        return sparse.kron(op_eigen_basis, sparse.identity(zeta_dim, format='csc', dtype=np.complex_), format='csc')

    def i_d_dphi_operator(self, zeropi_evecs=None):
        r"""
    Operator :math:`i d/d\varphi`.

    Returns
    -------
        scipy.sparse.csc_matrix
    """
        return self._zeropi_operator_in_product_basis(self._zeropi.i_d_dphi_operator(), zeropi_evecs=zeropi_evecs)

    def n_theta_operator(self, zeropi_evecs=None):
        r"""
        Operator :math:`n_\theta`.

        Returns
        -------
        scipy.sparse.csc_matrix
        """
        return self._zeropi_operator_in_product_basis(self._zeropi.n_theta_operator(), zeropi_evecs=zeropi_evecs)

    def phi_operator(self, zeropi_evecs=None):
        r"""
        Operator :math:`\varphi`.

        Returns
        -------
            scipy.sparse.csc_matrix
        """
        return self._zeropi_operator_in_product_basis(self._zeropi.phi_operator(), zeropi_evecs=zeropi_evecs)

    def hilbertdim(self):
        """Returns Hilbert space dimension"""
        return self.zeropi_cutoff * self.zeta_cutoff

    def _evals_calc(self, evals_count, hamiltonian_mat=None):
        if hamiltonian_mat is None:
            hamiltonian_mat = self.hamiltonian()
        evals = sparse.linalg.eigsh(hamiltonian_mat, k=evals_count, return_eigenvectors=False, which='SA')
        return np.sort(evals)

    def _esys_calc(self, evals_count, hamiltonian_mat=None):
        if hamiltonian_mat is None:
            hamiltonian_mat = self.hamiltonian()
        evals, evecs = sparse.linalg.eigsh(hamiltonian_mat, k=evals_count, return_eigenvectors=True, which='SA')
        evals, evecs = order_eigensystem(evals, evecs)
        return evals, evecs

    def g_phi_coupling_matrix(self, zeropi_states):
        """Returns a matrix of coupling strengths g^\\phi_{ll'} [cmp. Dempster et al., Eq. (18)], using the states
        from the list `zeropi_states`. Most commonly, `zeropi_states` will contain eigenvectors of the
        `DisorderedZeroPi` type.
        """
        # prefactor = self.EL * self.dEL * (8.0 * self.EC / self.EL)**0.25
        prefactor = self.EL * (self.dEL / 2.0) * (8.0 * self.EC / self.EL) ** 0.25
        return prefactor * get_matrixelement_table(self._zeropi.phi_operator(), zeropi_states)

    def g_theta_coupling_matrix(self, zeropi_states):
        """Returns a matrix of coupling strengths i*g^\\theta_{ll'} [cmp. Dempster et al., Eq. (17)], using the states
        from the list 'zeropi_states'.
        """
        prefactor = 1j * self.ECS() * (self.dC / 2.0) * (32.0 * self.EL / self.EC) ** 0.25
        return prefactor * get_matrixelement_table(self._zeropi.n_theta_operator(), zeropi_states)

    def g_coupling_matrix(self, zeropi_states=None, evals_count=None):
        """Returns a matrix of coupling strengths g_{ll'} [cmp. Dempster et al., text above Eq. (17)], using the states
        from 'zeropi_states'. If `zeropi_states==None`, then a set of `self.zeropi` eigenstates is calculated. Only in
        that case is `evals_count` used for the eigenstate number (and hence the coupling matrix size).
        """
        if evals_count is None:
            evals_count = self._zeropi.truncated_dim
        if zeropi_states is None:
            _, zeropi_states = self._zeropi.eigensys(evals_count=evals_count)
        return self.g_phi_coupling_matrix(zeropi_states) + self.g_theta_coupling_matrix(zeropi_states)

    def filewrite_params_h5(self, h5file_root):
        """Write current qubit parameters into a given h5 data file.

        Parameters
        ----------
        h5file_root: open h5py file
        """
        super().filewrite_params_h5(h5file_root)
        self.grid.filewrite_params_h5(h5file_root)

    def set_params_from_h5(self, h5file_root):
        """Read and store parameters from open h5 file

        Parameters
        ----------
        h5file_root: h5py.Group
            handle to root group in open h5 file
        """
        super().set_params_from_h5(h5file_root)
        grid_attrs = h5file_root.get('grid').attrs
        self.grid.min_val = grid_attrs['min_val']
        self.grid.max_val = grid_attrs['max_val']
        self.grid.pt_count = grid_attrs['pt_count']

        self._zeropi = ZeroPi(
            EJ=self.EJ,
            EL=self.EL,
            ECJ=self.ECJ,
            EC=self.EC,
            dEJ=self.dEJ,
            dCJ=self.dCJ,
            flux=self.flux,
            ng=self.ng,
            grid=self.grid,
            ncut=self.ncut,
            truncated_dim=self.zeropi_cutoff
        )
