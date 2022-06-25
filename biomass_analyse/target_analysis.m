covid_path = 'C:\Users\Administrator\Desktop\My_Research\data\covid\result_epsilon\';
dirs = dir(covid_path);
%读取所有样本目录
file_list={};
save_path='C:\Users\Administrator\Desktop\biomass_covid\biomass\epsilon';

for i=1:size(dirs,1)
    isdir=dirs(i).isdir;
    if isdir==1
        name=dirs(i).name;
        if ~isempty(strfind(name,'GSE')) && ~isempty(strfind(name,'infect')) && isempty(strfind(name,'pan'))
            file_list=[file_list;name];
        end
    end
end

if size(file_list,1)==1
    file_list=file_list';
end

load('C:\Users\Administrator\Desktop\My_Research\data\covid\group.mat');

target_patient_lung={};
target_patient_NasopharyngealSwab={};
target_patient={};
target_infect_lung={};
target_infect_nasal={};
target_infect_Bronchial={};
target_infect={};
all_target={};

for i = 1:size(file_list,1)
    series_name = file_list{i};
    cur_path = strcat(covid_path,series_name,'\');
    load(strcat(cur_path,'target.mat'));
    target=['Cal_Num_Gene';target];
    [~,loc]=ismember(series_name,name_group);
    if loc<=0
        disp(strcat(series_name,' not in any name group'));
        continue;
    end
    cur_sour=source_group{loc};
    cur_cell=cell_group{loc};
    all_target=[all_target;target];
    if strcmp(cur_sour,'patient')
        target_patient=[target_patient;target];
        if strcmp(cur_cell,'Lung')
            target_patient_lung=[target_patient_lung;target];
        elseif strcmp(cur_cell,'NasopharyngealSwab')
            target_patient_NasopharyngealSwab=[target_patient_NasopharyngealSwab;target];
        else
            disp(strcat(series_name,' not in any cell type'));
        end
    elseif strcmp(cur_sour,'infect')
        target_infect=[target_infect;target];
        if strcmp(cur_cell,'Lung')
            target_infect_lung=[target_infect_lung;target];
        elseif strcmp(cur_cell,'Nasal')
            target_infect_nasal=[target_infect_nasal;target];
        elseif strcmp(cur_cell,'Bronchial')
            target_infect_Bronchial=[target_infect_Bronchial;target];
        else
            disp(strcat(series_name,' not in any cell type'));
        end
    else
        disp(strcat(series_name,' not in any source'))
    end
    
    
    
end
table=tabulate(all_target);
sort=sortrows(table,-2);
%{
table_patient=tabulate(target_patient);
sort_patient=sortrows(table_patient,-2);

table_patient_lung=tabulate(target_patient_lung);
sort_patient_lung=sortrows(table_patient_lung,-2);

table_patient_NasopharyngealSwab=tabulate(target_patient_NasopharyngealSwab);
sort_patient_NasopharyngealSwab=sortrows(table_patient_NasopharyngealSwab,-2);
%}
table_infect=tabulate(target_infect);
sort_infect=sortrows(table_infect,-2);

table_infect_lung=tabulate(target_infect_lung);
sort_infect_lung=sortrows(table_infect_lung,-2);

table_infect_nasal=tabulate(target_infect_nasal);
sort_infect_nasal=sortrows(table_infect_nasal,-2);

table_infect_Bronchial=tabulate(target_infect_Bronchial);
sort_infect_Bronchial=sortrows(table_infect_Bronchial,-2);

save(strcat(save_path,'\sort.mat'),'sort');
save(strcat(save_path,'\sort_infect.mat'),'sort_infect');
save(strcat(save_path,'\sort_infect_lung.mat'),'sort_infect_lung');
save(strcat(save_path,'\sort_infect_nasal.mat'),'sort_infect_nasal');
save(strcat(save_path,'\sort_infect_Bronchial.mat'),'sort_infect_Bronchial');