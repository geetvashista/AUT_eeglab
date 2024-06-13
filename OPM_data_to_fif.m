% Load and set parameters
load("sub-001_task-movie_run-001_meg.mat") % raw matlab array
samplingFrequency = 1200; % Sampling frequency
xyzCoordinates = '<- COORDINATES PATH ->'; % xyz file set as 3 colombes by 168 rows

% Add FieldTrip toolbox to MATLAB path
addpath(' <- FIELDREIP PATH -> ');

% import FieldTrip
ft_defaults;

% FieldTrip data structure
raw_data = data;
data = [];
data.trial{1} = raw_data;
data.time{1} = 0:1/samplingFrequency:(size(raw_data, 2) - 1) / samplingFrequency;
data.label = cell(1, size(raw_data, 1));
for i = 1:size(raw_data, 1)
    data.label{i} = ['MEG' num2str(i)];
end
data.fsample = samplingFrequency;

% xyz coordinates to the data
data.grad = struct();
data.grad.chanpos = xyzCoordinates;
data.grad.label = data.label;

% Set channel types to MEG
for i = 1:numel(data.label)
    data.grad.chantype{i} = 'meg';
end

% configure data
cfg = [];
cfg.dataset = data;
cfg.channel = 'all';
OPM_data = ft_preprocessing(cfg);

% Save the data as .fif file
fieldtrip2fiff('OPM_data.fif', OPM_data);