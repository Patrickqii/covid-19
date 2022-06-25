clear
addpath('C:\Users\Administrator\Desktop\biomass_covid\biomass');
Save_Path='C:\Users\Administrator\Desktop\biomass_covid\biomass';
filename = 'biomass.txt';
fid=fopen(filename);  %���ı��ļ�
while ~feof(fid)
    biomass = fgetl(fid);   % ��ȡһ��, str���ַ���
    %splitStr = regexp(str ,'\,','split');   % ��str�е�comma��Ϊ�ָ����ݵ��ַ����˴���������Զ�ȡ���ı�������Ӧ�Ĳ�������
end
fclose(fid);
Output_File_Name='equation';
equation={};
equation{end+1}=biomass;
save(strcat(Save_Path,'\',Output_File_Name,'.mat'),'equation');
varient={'alpha','beta','gamma','epsilon'};
for i=1:length(varient)
   filename=strcat('biomass_',varient{i},'.txt');
   fid=fopen(filename);  %���ı��ļ�
   while ~feof(fid)
        biomass = fgetl(fid);   % ��ȡһ��, str���ַ���
        %splitStr = regexp(str ,'\,','split');   % ��str�е�comma��Ϊ�ָ����ݵ��ַ����˴���������Զ�ȡ���ı�������Ӧ�Ĳ�������
    end
    fclose(fid);
    Output_File_Name=strcat('equation_',varient{i});
    equation={};
    equation{end+1}=biomass;
    save(strcat(Save_Path,'\',Output_File_Name,'.mat'),'equation');
end
    
rmpath('C:\Users\Administrator\Desktop\biomass_covid\biomass');