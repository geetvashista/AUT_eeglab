% Load and set parameters
load("sub-001_task-movie_run-001_meg.mat") % raw matlab array
ch_table = readtable('sub-001_task-movie_run-001_channels.tsv_new',...
                'Delimiter','tab','FileType','text');

samplingFrequency = 1200; % Sampling frequency

% import FieldTrip
ft_defaults;

% FieldTrip data structure
raw_data = data';

%% sensor info
S.sensor_info.pos = [ch_table.Px ch_table.Py ch_table.Pz];
S.sensor_info.ors = [ch_table.Ox ch_table.Oy ch_table.Oz];

%% Mean field correction
N = S.sensor_info.ors; % orientation matrix (N_sens x 3)
S.M = eye(length(N)) - N*pinv(N);

%% Put data in FT format
disp("Converting to FieldTrip format")
OPM_data = makeFTstruct(raw_data,fs,ch_table,S.sensor_info);

% Save the data as .fif file
fieldtrip2fiff('OPM_data.fif', OPM_data);