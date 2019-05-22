folder = 'C:\Users\Eric Minor\TrackingML\defectTracker\imagesCLEAN\';
ext = 'jpg';

annotateFolder = strcat(folder,'houghAnnotated');
hImgFolder = strcat(folder,'houghImage');

if ~exist(annotateFolder,'dir')
   mkdir(annotateFolder) 
end

if ~exist(hImgFolder,'dir')
   mkdir(hImgFolder) 
end

imageNames = dir(fullfile(folder, strcat('*.',ext)));
numImgs = length(imageNames);

name = strcat(imageNames(1).folder,'\',imageNames(1).name);
img = imread(name);
%imshow(img)



[centers, radii, metric] = imfindcircles(img,[4 20],'Sensitivity',0.90);
%viscircles(centers,radii,'EdgeColor','b');


for i =1:numImgs
    name = strcat(imageNames(i).folder,'\',imageNames(i).name);
    nameImg = strcat(hImgFolder,'\',imageNames(i).name);
    
    nameParts = split(imageNames(i).name,'.');
    justName = nameParts(1);
    
    nameAnno = strcat(annotateFolder,'\',justName,'.txt');
    img = imread(name);
    imshow(img)
    [centers, radii, metric] = imfindcircles(img,[4 20],'Sensitivity',0.90);
    viscircles(centers,radii,'EdgeColor','b');
    saveas(gcf,nameImg);

    fileID = fopen(nameAnno{1},'w');
    numCirc = length(radii);
    fprintf(fileID,'%d\r\n',numCirc);
    for j=1:numCirc
        fprintf(fileID,'%d %d %d %d\r\n',[uint8(centers(j,1)-10),uint8(centers(j,2)-10),uint8(centers(j,1)+10),uint8(centers(j,2)+10)]);

    end
    fclose(fileID);
   
   
   %imshow(rotatedImg);
   %imwrite(rotatedImg,nameOut)
end