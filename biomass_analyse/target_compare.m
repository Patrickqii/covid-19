addpath('C:\Users\Administrator\Desktop\biomass_covid\biomass');
path='C:\Users\Administrator\Desktop\biomass_covid\biomass';
load(strcat(path,'\alpha\sort_infect.mat'))
sort_infect_alpha=sort_infect;
load(strcat(path,'\beta\sort_infect.mat'))
sort_infect_beta=sort_infect;
load(strcat(path,'\gamma\sort_infect.mat'))
sort_infect_gamma=sort_infect;
load(strcat(path,'\epsilon\sort_infect.mat'))
sort_infect_epsilon=sort_infect;
load(strcat(path,'\sars-cov2\sort_infect.mat'))

iseq_alpha=isequal(sort_infect,sort_infect_alpha);
iseq_beta=isequal(sort_infect,sort_infect_beta);
iseq_gamma=isequal(sort_infect,sort_infect_gamma);
iseq_epsilon=isequal(sort_infect,sort_infect_epsilon);
rmpath('C:\Users\Administrator\Desktop\biomass_covid\biomass');
