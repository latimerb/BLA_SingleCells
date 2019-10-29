from bmtk.simulator.bionet.pyfunction_cache import add_synapse_model
from neuron import h

pc = h.ParallelContext()

#Static variable for entire execution, may be a better method
class GAPCounter:
    i = 2

def InhSyn(syn_params, sec_x, sec_id):
    """Create a inhsyn synapse
    :param syn_params: parameters of a synapse
    :param sec_x: normalized distance along the section
    :param sec_id: target section
    :return: NEURON synapse object
    """

    lsyn = h.inhsyn(sec_x, sec=sec_id)

    if syn_params.get('esyn'):
        lsyn.esyn = float(syn_params['esyn'])
    if syn_params.get('gmax'):
        lsyn.gmax = float(syn_params['gmax'])
		
    return lsyn

def inhsyn(syn_params, xs, secs):
    """Create a list of inhsyn synapses
    :param syn_params: parameters of a synapse
    :param xs: list of normalized distances along the section
    :param secs: target sections
    :return: list of NEURON synpase objects
    """
    syns = []
    for x, sec in zip(xs, secs):
        syn = InhSyn(syn_params, x, sec)
        syns.append(syn)
    return syns

def GAP(syn_params, sec_x, sec_id):
    gap_syn = h.GAP(sec_x, sec=sec_id)
    #import pdb
    #pdb.set_trace()    
    if syn_params.get('setpointer'):
        target_var_name = syn_params['setpointer']
        target_var = eval("gap_syn._ref_{}".format(target_var_name))
        pc.target_var(target_var, GAPCounter.i)
    if syn_params.get('r'):
        gap_syn.r = syn_params['r']

    target_gid = GAPCounter.i
    GAPCounter.i = GAPCounter.i + 1 
    return gap_syn, target_gid

def gap(syn_params, xs, secs):
    syns = []
    for x, sec in zip(xs, secs):
        syn = GAP(syn_params, x, sec)
        syns.append(syn)
    return syns


def load():
    add_synapse_model(InhSyn, 'inhsyn', overwrite=False)
    add_synapse_model(InhSyn, overwrite=False)
    add_synapse_model(GAP,'GAP',overwrite=False)
    add_synapse_model(GAP,overwrite=False)
    return
