from pysph.base.utils import get_particle_array


def get_particle_array_pcisph(constants=None, **props):
    pcisph_props = ['ao_x', 'ao_y', 'ao_z', 'ap_x', 'ap_y', 'ap_z', 'rho_err']

    # compression factor
    consts = {'delta': [0.0]}
    if constants:
        consts.update(constants)

    pa = get_particle_array(
        constants=consts, additional_props=pcisph_props, **props
    )
    pa.set_output_arrays(['x', 'y', 'z', 'u', 'v', 'w', 'rho', 'h', 'm',
                          'p', 'pid', 'au', 'av', 'aw', 'tag', 'gid', 'V'])
    return pa
