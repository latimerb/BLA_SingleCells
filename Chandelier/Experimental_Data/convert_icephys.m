%% NWB file
% All contents get added to the NWB file, which is created with the
% following command

date = datetime(2018, 3, 1, 12, 0, 0);
session_start_time = datetime(date, ...
    'Format', 'yyyy-MM-dd''T''HH:mm:ssZZ', ...
    'TimeZone', 'local');

nwb = nwbfile( ...
    'session_description', 'a test NWB File', ...
    'identifier', 'mouse004_day4', ...
    'session_start_time', session_start_time);

%%
% You can check the contents by displaying the nwbfile object
disp(nwb);

%% Subject
% Subject-specific information goes in type |Subject| in location 
% |general_subject|.

nwb.general_subject = types.core.Subject( ...
    'description', 'mouse 5', 'age', '9 months', ...
    'sex', 'M', 'species', 'Mus musculus');

%% Set up meta-data

device_name = 'Heka ITC-1600';
nwb.general_devices.set(device_name, types.core.Device());
device_link = types.untyped.SoftLink(['/general/devices/' device_name]);

ic_elec = types.core.IntracellularElectrode( ...
    'device', device_link, ...
    'description', 'my description');

ic_elec_name = 'ic_elec';
nwb.general_intracellular_ephys.set(ic_elec_name, ic_elec)

ic_elec_link = types.untyped.SoftLink(['/general/intracellular_ephys/' ic_elec_name]);


%% membrane potential
% Intracellular stimulus and response data are represented with subclasses 
% of PatchClampSeries. There are two classes for representing stimulus 
% data?VoltageClampStimulusSeries and CurrentClampStimulusSeries?, and 
% three classes for representing response data?VoltageClampSeries, 
% VoltageClampSeries, CurrentClampSeries, and IZeroClampSeries.

data_in = load('Chn.mat');
tt = data_in.c001_Time;

fn = fieldnames(data_in);

nwb.stimulus_presentation.set('voltag_stimulus', ...
    types.core.CurrentClampStimulusSeries( ...
        'electrode', ic_elec_link, ...
        'gain', NaN, ...
        'stimulus_description', 'my description', ...
        'data_unit', 'mA', ...
        'data', ones(1,100), ...
        'timestamps', tt));

for k=1:numel(fn)
    if ~strcmp(fn{k}, 'c001_Time')
        data = data_in.(fn{k});
        nwb.acquisition.set(fn{k}, ...
            types.core.CurrentClampSeries( ...
                'bias_current', [], ... % Unit: Amp
                'bridge_balance', [], ... % Unit: Ohm
                'capacitance_compensation', [], ... % Unit: Farad
                'timestamps', tt, ... % seconds
                'data', data, ...
                'data_unit', 'V', ...
                'electrode', ic_elec_link, ...
                'stimulus_description', 'description of stimulus'));        
    end
end

% similar for the other data types

%% write

nwbExport(nwb, 'test_icephys_out.nwb');

%% read

nwb_in = nwbRead('test_icephys_out.nwb');

mem_pot_1 = nwb_in.acquisition.get('c002_Membrane_Voltage_1');

mem_pot_1.data.load
