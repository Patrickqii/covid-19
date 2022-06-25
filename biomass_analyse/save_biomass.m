clear
addpath('C:\Users\Administrator\Desktop\biomass_covid\biomass');
Save_Path='C:\Users\Administrator\Desktop\biomass_covid\biomass';
filename = 'biomass.txt';
fid=fopen(filename);  %打开文本文件
while ~feof(fid)
    biomass = fgetl(fid);   % 读取一行, str是字符串
    %splitStr = regexp(str ,'\,','split');   % 以str中的comma作为分割数据的字符。此处根据需求对读取的文本进行相应的操作即可
end
fclose(fid);
Output_File_Name='equation';
equation={};
equation{end+1}=biomass;
save(strcat(Save_Path,'\',Output_File_Name,'.mat'),'equation');
varient={'alpha','beta','gamma','epsilon'};
for i=1:length(varient)
   filename=strcat('biomass_',varient{i},'.txt');
   fid=fopen(filename);  %打开文本文件
   while ~feof(fid)
        biomass = fgetl(fid);   % 读取一行, str是字符串
        %splitStr = regexp(str ,'\,','split');   % 以str中的comma作为分割数据的字符。此处根据需求对读取的文本进行相应的操作即可
    end
    fclose(fid);
    Output_File_Name=strcat('equation_',varient{i});
    equation={};
    equation{end+1}=biomass;
    save(strcat(Save_Path,'\',Output_File_Name,'.mat'),'equation');
end
    
rmpath('C:\Users\Administrator\Desktop\biomass_covid\biomass');