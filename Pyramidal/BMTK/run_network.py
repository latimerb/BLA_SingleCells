from bmtk.simulator import bionet
from bmtk.simulator.bionet.default_setters.cell_models import loadHOC

# Load hoc cell templates
bionet.pyfunction_cache.add_cell_model(loadHOC, directive='hoc', model_type='biophysical')

conf = bionet.Config.from_json('PN_IClamp/simulation_config.json')
conf.build_env()
net = bionet.BioNetwork.from_config(conf)
sim = bionet.BioSimulator.from_config(conf, network=net)
sim.run()
