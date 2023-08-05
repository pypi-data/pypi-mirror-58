# -*- coding: utf-8 -*-

"""NPT (canonical) dynamics in LAMMPS"""

import lammps_step
import logging
import seamm
from seamm_util import ureg, Q_, units_class  # noqa: F401
import seamm_util.printing as printing
from seamm_util.printing import FormattedText as __
import random

logger = logging.getLogger(__name__)
job = printing.getPrinter()
printer = printing.getPrinter('lammps')


class NPT(lammps_step.NVT):

    methods = {
        'Nose-Hoover':
            {
                'documentation':
                    'https://lammps.sandia.gov/doc/fix_nh.html#fix-npt-command',  # noqa: E501
                'references': ['Shinoda', 'Tuckerman'],
            },
        'Berendsen':
            {
                'documentation':
                    'https://lammps.sandia.gov/doc/fix_press_berendsen.html',  # noqa: E501
                'references': ['Berendsen'],
            },
    }

    references = {
        'Shinoda':
            {
                'bibtex':
                    """
                @article{PhysRevB.69.134103,
                  title = {Rapid estimation of elastic constants by molecular dynamics simulation under constant stress},
                  author = {Shinoda, Wataru and Shiga, Motoyuki and Mikami, Masuhiro},
                  journal = {Phys. Rev. B},
                  volume = {69},
                  issue = {13},
                  pages = {134103},
                  numpages = {8},
                  year = {2004},
                  month = {Apr},
                  publisher = {American Physical Society},
                  doi = {10.1103/PhysRevB.69.134103},
                  url = {https://link.aps.org/doi/10.1103/PhysRevB.69.134103}
            }"""  # noqa: E501
            },
        'Tuckerman':
            {
                'bibtex':
                    """
                @article{0305-4470-39-19-S18,
                  author={Mark E Tuckerman and José Alejandre and Roberto López-Rendón and Andrea L Jochim and Glenn J Martyna},
                  title={A Liouville-operator derived measure-preserving integrator for molecular dynamics simulations in the isothermal–isobaric ensemble},
                  journal={Journal of Physics A: Mathematical and General},
                  volume={39},
                  number={19},
                  pages={5629},
                  url={http://stacks.iop.org/0305-4470/39/i=19/a=S18},
                  year={2006},
                  abstract={The constant-pressure,
                  constant-temperature ( NPT ) molecular dynamics
                  approach is re-examined from the viewpoint of
                  deriving a new measure-preserving reversible
                  geometric integrator for the equations of
                  motion. The underlying concepts of non-Hamiltonian
                  phase-space analysis, measure-preserving integrators
                  and the symplectic property for Hamiltonian systems
                  are briefly reviewed. In addition, current
                  measure-preserving schemes for the constant-volume,
                  constant-temperature ensemble are also reviewed. A
                  new geometric integrator for the NPT method is
                  presented, is shown to preserve the correct
                  phase-space volume element and is demonstrated to
                  perform well in realistic examples. Finally, a
                  multiple time-step version of the integrator is
                  presented for treating systems with motion on
                  several time scales.}
            }"""  # noqa: E501
            },
        'Berendsen':
            {
                'bibtex':
                    """
                @article{doi:10.1063/1.448118,
                author = {H. J. C. Berendsen and J. P. M. Postma and W. F. van Gunsteren and A. DiNola and J. R. Haak},
                title = {Molecular dynamics with coupling to an external bath},
                journal = {The Journal of Chemical Physics},
                volume = {81},
                number = {8},
                pages = {3684-3690},
                year = {1984},
                doi = {10.1063/1.448118},
                URL = {https://doi.org/10.1063/1.448118},
                eprint = {https://doi.org/10.1063/1.448118}
            }"""  # noqa: E501
            },
    }

    def __init__(self, flowchart=None, title='NPT dynamics', extension=None):
        """Initialize the node"""

        logger.debug('Creating NPT {}'.format(self))

        super().__init__(flowchart=flowchart, title=title, extension=extension)

        logger.debug('NPT after super init, {}'.format(self))

        self.description = 'NPT dynamics step in LAMMPS'

        logger.debug("NPT.init() creating NPT_Parameters object")

        self.parameters = lammps_step.NPT_Parameters()

        logger.debug("NPT.init() completed")

    def description_text(self, P=None):
        """Create the text description of what this step will do.
        The dictionary of control values is passed in as P so that
        the code can test values, etc.
        """

        if not P:
            P = self.parameters.values_to_dict()

        # What will we do?

        if P['T0'] == P['T1']:
            text = "{time} of canonical (NPT) dynamics at {T0} "
        else:
            text = (
                "{time} of canonical (NPT) dynamics starting "
                " at {T0}, going to {T1}, "
            )
        if P['thermostat'] == 'Nose-Hoover':
            text += "using a Nose-Hoover thermostat."
            if P['Tchain'] != '3':
                if P['Tloop'] != '1':
                    text += (
                        " The thermostat will use a chain of {Tchain} "
                        "thermostats with {Tloop} subcycles and a "
                    )
                else:
                    text += (
                        " The thermostat will use a chain of {Tchain} "
                        "thermostats and a "
                    )
            elif P['Tloop'] != '1':
                text += " The thermostat will use {Tloop} subcycles and a "
            else:
                text += " The thermostat will use a "
            text += "drag factor of {drag}."
        elif P['thermostat'] == 'Berendsen':
            text += (
                "using a Berendsen thermostat with a damping time "
                "of {Tdamp}"
            )
        elif 'csvr' in P['thermostat']:
            text += (
                "using a canonical sampling thermostat using velocity "
                "rescaling (CSVR) with a damping time of {Tdamp} and "
                "a {random_seed}."
            )
        elif 'csld' in P['thermostat']:
            text += (
                "using a canonical sampling thermostat using Langevin "
                "dynamics (CSLD) with a damping time of {Tdamp} and "
                "a {random_seed}."
            )
        elif P['thermostat'] == 'velocity rescaling':
            text += (
                "using velocity rescaling every {frequency} with a "
                "temperature window of {window}."
            )
            if P['fraction'] != 1.0:
                text += (
                    " The velocities will only be scaled a fraction "
                    "({fraction}) of the amount needed to fully correct "
                    "the temperature."
                )
        elif P['thermostat'] == 'Langevin':
            text += (
                "using a Langevin thermostat with a damping time "
                "of {Tdamp} and a {random_seed}"
            )
        else:
            text += ("using the thermostat given by {thermostat}")

        return self.header + '\n' + __(text, **P, indent=4 * ' ').__str__()

    def describe(self, indent='', json_dict=None):
        """Write out information about what this node will do
        If json_dict is passed in, add information to that dictionary
        so that it can be written out by the controller as appropriate.
        """

        # Can't call super() because it will print too much
        self.visited = True
        job.job('\n' + self.indent + self.header)
        next_node = self.next()

        # Local copies of variables in a dictionary

        P = self.parameters.values_to_dict()
        text = self.description_text(P)
        job.job(__(text, indent=self.indent + '    ', **P))

        return next_node

    def get_input(self):
        """Get the input for an NPT dynamics run in LAMMPS"""

        keep_orthorhombic = True

        self.description = []

        P = self.parameters.current_values_to_dict(
            context=seamm.flowchart_variables._data
        )

        # Fix variables with special cases

        # These need to be based on masses...
        if P['timestep'] == 'normal':
            timestep = 1.0
            P['timestep'] = Q_(timestep, ureg.fs)
        elif P['timestep'] == 'accurate but slow':
            timestep = 0.5
            P['timestep'] = Q_(timestep, ureg.fs)
        elif P['timestep'] == 'coarse but fast':
            timestep = 2.0
            P['timestep'] = Q_(timestep, ureg.fs)
        else:
            timestep = P['timestep'].to('fs').magnitude

        if P['seed'] == 'random':
            P['seed'] = int(random.random() * 2**31)

        # Have to fix formatting for printing...
        PP = dict(P)
        for key in PP:
            if isinstance(PP[key], units_class):
                PP[key] = '{:~P}'.format(PP[key])

        self.description.append(
            __(self.description_text(PP), **PP, indent=3 * ' ')
        )

        time = P['time'].to('fs').magnitude
        nsteps = round(time / timestep)

        thermo_properties = (
            'time temp press etotal ke pe ebond '
            'eangle edihed eimp evdwl etail ecoul elong'
        )
        properties = (
            'v_time v_temp v_press v_density v_cella v_cellb '
            'v_cellc v_etotal v_ke v_pe v_epair'
        )
        titles = 'tstep t T P density a b c Etot Eke Epe Epair'

        T0 = P['T0'].to('K').magnitude
        T1 = P['T1'].to('K').magnitude
        Tdamp = P['Tdamp'].to('fs').magnitude

        barostat = P['barostat']
        if barostat == 'Berendsen':
            modulus = P['modulus'].to('atm').magnitude

        # Work out the pressure/stress part of the command
        ptext = self.get_pressure_text(P, keep_orthorhombic)

        # and build the LAMMPS script
        lines = []
        lines.append('')
        lines.append('#     NPT dynamics')
        lines.append('')
        lines.append('reset_timestep      0')
        lines.append('timestep            {}'.format(timestep))
        lines.append('thermo_style        custom {}'.format(thermo_properties))
        lines.append('thermo              {}'.format(int(nsteps / 100)))

        nfixes = 0
        if P['thermostat'] == 'Nose-Hoover':
            Tchain = P['Tchain']
            Tloop = P['Tloop']
            drag = P['drag']
            if barostat == 'Nose-Hoover':
                nfixes += 1
                lines.append(
                    'fix                 {} all npt '.format(nfixes) +
                    'temp {} {} {} '.format(T0, T1, Tdamp) +
                    'tchain {} '.format(Tchain) + 'tloop {} '.format(Tloop) +
                    'drag {}'.format(drag) + ptext
                )
            else:
                nfixes += 1
                lines.append(
                    'fix                 {} all nvt '.format(nfixes) +
                    'temp {} {} {} '.format(T0, T1, Tdamp) +
                    'tchain {} '.format(Tchain) + 'tloop {} '.format(Tloop) +
                    'drag {}'.format(drag)
                )
                nfixes += 1
                lines.append(
                    'fix                 {} all '.format(nfixes) +
                    'press/berendsen ' + ptext + ' modulus {}'.format(modulus)
                )
        elif P['thermostat'] == 'Berendsen':
            nfixes += 1
            lines.append(
                'fix                 {} '.format(nfixes) +
                'all temp/berendsen ' + ' {} {} {}'.format(T0, T1, Tdamp)
            )
            nfixes += 1
            lines.append('fix                 {} '.format(nfixes) + 'all nve')
        elif 'csvr' in P['thermostat']:
            seed = P['seed']
            nfixes += 1
            lines.append(
                'fix                 {} '.format(nfixes) + 'all temp/csvr ' +
                ' {} {} {} {}'.format(T0, T1, Tdamp, seed)
            )
            nfixes += 1
            lines.append('fix                 {} '.format(nfixes) + 'all nve')
        elif 'csld' in P['thermostat']:
            seed = P['seed']
            nfixes += 1
            lines.append(
                'fix                 {} '.format(nfixes) + 'all temp/csld ' +
                ' {} {} {} {}'.format(T0, T1, Tdamp, seed)
            )
            nfixes += 1
            lines.append('fix                 {} '.format(nfixes) + 'all nve')
        elif P['thermostat'] == 'velocity rescaling':
            frequency = P['frequency']
            nevery = round(nsteps / (frequency / timestep))
            window = P['window'].to('K').magnitude
            fraction = P['fraction']
            nfixes += 1
            lines.append(
                'fix                 {} '.format(nfixes) +
                'all temp/rescale ' +
                '{} {} {} {} {}'.format(nevery, T0, T1, window, fraction)
            )
            nfixes += 1
            lines.append('fix                 {} '.format(nfixes) + 'all nve')
        elif P['thermostat'] == 'Langevin':
            seed = P['seed']
            nfixes += 1
            lines.append(
                'fix                 {} '.format(nfixes) + 'all langevin ' +
                '{} {} {} {} '.format(T0, T1, Tdamp, seed)
            )
            nfixes += 1
            lines.append('fix                 {} '.format(nfixes) + 'all nve')
        else:
            raise RuntimeError(
                "Don't recognize temperature control " +
                "'{}'".format(P['thermostat'])
            )

        # summary output written 10 times during run so we can see progress
        nevery = 10
        nfreq = int(nsteps / 10)
        nrepeat = int(nfreq / nevery)
        nfreq = nevery * nrepeat
        nfixes += 1
        lines.append(
            'fix                 {} '.format(nfixes) + 'all ave/time ' +
            "{} {} {} {} off 2 title2 '{}' file summary_npt_{}.txt".format(
                nevery, nrepeat, nfreq, properties, titles,
                '_'.join(str(e) for e in self._id)
            )
        )
        # instantaneous output written for averaging
        if P['sampling'] == 'none':
            self.decription.append(
                __(
                    "The run will be {nsteps:n} steps of dynamics.",
                    nsteps=nsteps,
                    indent=3 * ' '
                )
            )
        else:
            sampling = P['sampling'].to('fs').magnitude
            nevery = round(sampling / timestep)
            nfreq = int(nsteps / nevery)
            nrepeat = 1
            nfreq = nevery * nrepeat
            nfixes += 1
            lines.append(
                'fix                 {} '.format(nfixes) + 'all ave/time ' +
                "{} {} {} {} off 2 title2 '{}' file trajectory_npt_{}.txt"
                .format(
                    nevery, nrepeat, nfreq, properties, titles,
                    '_'.join(str(e) for e in self._id)
                )
            )
            self.description.append(
                __(
                    (
                        "The run will be {nsteps:,d} steps of dynamics "
                        "sampled every {nevery:n} steps."
                    ),
                    nsteps=nsteps,
                    nevery=nevery,
                    indent=7 * ' '
                )
            )

        lines.append('run                 {}'.format(nsteps))
        lines.append('')
        for fix in range(1, nfixes + 1):
            lines.append('unfix               {}'.format(fix))

        return lines

    def get_pressure_text(self, P, keep_orthorhombic):
        """Work out and return the pressure/stress part of the
        'fix npt' or 'fix berendsen' in LAMMPS
        """
        system_type = P['system type']
        Panneal = P['Panneal']
        if system_type == 'fluid':
            use_stress = 'isotropic pressure'
            couple = 'x, y and z'
        else:
            use_stress = P['use_stress']
            couple = P['couple']

        if use_stress == 'isotropic pressure':
            if couple == 'x, y and z':
                if keep_orthorhombic:
                    ptext = ' iso {P0} {P1} {Pdamp}'
                else:
                    ptext = (
                        ' couple xyz '
                        'x {P0} {P1} {Pdamp} '
                        'y {P0} {P1} {Pdamp} '
                        'z {P0} {P1} {Pdamp}'
                    )
                if not keep_orthorhombic:
                    ptext += (
                        ' xy 0.0 0.0 {Pdamp} '
                        'xz 0.0 0.0 {Pdamp} '
                        'yz 0.0 0.0 {Pdamp}'
                    )
            elif couple == 'x and y':
                ptext = (
                    ' couple xy '
                    'x {P0} {P1} {Pdamp} '
                    'y {P0} {P1} {Pdamp} '
                    'z {P0} {P1} {Pdamp}'
                )
                if not keep_orthorhombic:
                    ptext += (
                        ' xy 0.0 0.0 {Pdamp} '
                        'xz 0.0 0.0 {Pdamp} '
                        'yz 0.0 0.0 {Pdamp}'
                    )
            elif couple == 'x and z':
                ptext = (
                    ' couple xz '
                    'x {P0} {P1} {Pdamp} '
                    'y {P0} {P1} {Pdamp} '
                    'z {P0} {P1} {Pdamp}'
                )
                if not keep_orthorhombic:
                    ptext += (
                        ' xy 0.0 0.0 {Pdamp} '
                        'xz 0.0 0.0 {Pdamp} '
                        'yz 0.0 0.0 {Pdamp}'
                    )
            elif couple == 'y and z':
                ptext = (
                    ' couple yz '
                    'x {P0} {P1} {Pdamp} '
                    'y {P0} {P1} {Pdamp} '
                    'z {P0} {P1} {Pdamp}'
                )
                if not keep_orthorhombic:
                    ptext += (
                        ' xy 0.0 0.0 {Pdamp} '
                        'xz 0.0 0.0 {Pdamp} '
                        'yz 0.0 0.0 {Pdamp}'
                    )
            else:
                if keep_orthorhombic:
                    ptext = ' aniso {P0} {P1} {Pdamp}'
                else:
                    ptext = ' tri {P0} {P1} {Pdamp}'

            P0 = P['Pinitial'].to('atm').magnitude
            if Panneal:
                P1 = P['Pfinal'].to('atm').magnitude
            else:
                P1 = P0
            Pdamp = P['Pdamp'].to('fs').magnitude

            ptext = ptext.format(P0=P0, P1=P1, Pdamp=Pdamp)
        else:
            if couple == 'x, y and z':
                ptext = (
                    ' couple = xyz '
                    'x {Sxx0} {Sxx1} {Dxx} '
                    'y {Sxx0} {Sxx1} {Dxx} '
                    'z {Sxx0} {Sxx1} {Dxx}'
                )
            elif couple == 'x and y':
                ptext = (
                    ' couple = xy '
                    'x {Sxx0} {Sxx1} {Dxx} '
                    'y {Sxx0} {Sxx1} {Dxx} '
                    'z {Szz0} {Szz1} {Dzz}'
                )
            elif couple == 'x and z':
                ptext = (
                    ' couple = xz '
                    'x {Sxx0} {Sxx1} {Dxx} '
                    'y {Syy0} {Syy1} {Dyy} '
                    'z {Sxx0} {Sxx1} {Dxx}'
                )
            elif couple == 'y and z':
                ptext = (
                    ' couple = yz '
                    'x {Sxx0} {Sxx1} {Dxx} '
                    'y {Syy0} {Syy1} {Dyy} '
                    'z {Syy0} {Syy1} {Dyy}'
                )
            else:
                # elif couple == 'none':
                ptext = (
                    ' couple = none '
                    'x {Sxx0} {Sxx1} {Dxx} '
                    'y {Syy0} {Syy1} {Dyy} '
                    'z {Szz0} {Szz1} {Dzz}'
                )

            if not keep_orthorhombic:
                ptext += (
                    ' xy {Sxy0} {Sxy1} {Dxy} '
                    'xz {Sxz0} {Sxz1} {Dxz} '
                    'yz {Syz0} {Syz1} {Dyz}'
                )

            Tmp = {}
            Tmp['Sxx0'] = P['Sxx,initial'].to('atm').magnitude
            Tmp['Syy0'] = P['Syy,initial'].to('atm').magnitude
            Tmp['Szz0'] = P['Szz,initial'].to('atm').magnitude
            if Panneal:
                Tmp['Sxx1'] = P['Sxx,final'].to('atm').magnitude
                Tmp['Syy1'] = P['Syy,final'].to('atm').magnitude
                Tmp['Szz1'] = P['Szz,final'].to('atm').magnitude
            else:
                Tmp['Sxx1'] = Tmp['Sxx0']
                Tmp['Syy1'] = Tmp['Syy0']
                Tmp['Szz1'] = Tmp['Szz0']
            Tmp['Dxx'] = P['Sxx damp'].to('fs').magnitude
            Tmp['Dyy'] = P['Syy damp'].to('fs').magnitude
            Tmp['Dzz'] = P['Szz damp'].to('fs').magnitude

            if not keep_orthorhombic:
                Tmp['Sxy0'] = P['Sxy,initial'].to('atm').magnitude
                Tmp['Sxz0'] = P['Sxz,initial'].to('atm').magnitude
                Tmp['Syz0'] = P['Syz,initial'].to('atm').magnitude
                if Panneal:
                    Tmp['Sxy1'] = P['Sxy,final'].to('atm').magnitude
                    Tmp['Sxz1'] = P['Sxz,final'].to('atm').magnitude
                    Tmp['Syz1'] = P['Syz,final'].to('atm').magnitude
                else:
                    Tmp['Sxy1'] = Tmp['Sxy0']
                    Tmp['Sxz1'] = Tmp['Sxz0']
                    Tmp['Syz1'] = Tmp['Syz0']
                Tmp['Dxy'] = P['Sxy damp'].to('fs').magnitude
                Tmp['Dxz'] = P['Sxz damp'].to('fs').magnitude
                Tmp['Dyz'] = P['Syz damp'].to('fs').magnitude

            ptext = ptext.format(**Tmp)

        return ptext

    def analyze(self, indent='', data={}):
        """Parse the output and generating the text output and store the
        data in variables for other stages to access
        """

        # printer.normal(self._long_header)

        # Put any requested results into variables or tables
        self.store_results(
            data=data,
            properties=lammps_step.properties,
            results=self.parameters['results'].value,
            create_tables=self.parameters['create tables'].get()
        )

        # printer.normal('\n')
