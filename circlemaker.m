numImages = 200;


for i =1:numImages
    [img,circleX,circleY] = generateImg();
    imwrite(img, strcat('images/circle_',num2str(i),'.jpg'));
    fileID = fopen(strcat('labels/circle_',num2str(i),'.txt'),'w');
    numCirc = length(circleX);
    fprintf(fileID,'%d\r\n',numCirc);
    for j=1:numCirc
        fprintf(fileID,'%d %d %d %d\r\n',[circleY(j)+10,circleX(j)+10,circleY(j)-10,circleX(j)-10]);
        
    end
    fclose(fileID);
end




function [img,circleX,circleY] = generateImg()

    img = randi(255,250,250,'uint8');
    circleX = randi(230,1,5,'double')+10;
    circleY = randi(230,1,5,'double')+10;
    [Y,X] = meshgrid(1:250,1:250);
    %X = uint8(X);
    %Y = uint8(Y);
    numCents = length(circleX);

    for i =1:numCents
       circlePixels = sqrt((Y-circleY(i)).^2 + (X-circleX(i)).^2) <= 10;
       img(circlePixels) =  randi(255,1,1,'uint8');

    end
    img = imnoise(img,'gaussian');
    

    %valid = zeros(1024,1024,'logical');
    %[Y,X] = meshgrid(1:1024,1:1024);

    %img2 = genCircle(img,valid,X,Y);

    %imshow(img)

end




function img = genCircle(img,valid,X,Y)

    


end



function [seed,fail] = getSeed(valid,binPos,X,Y)

    %valid = validStack(:,:,binPos);
    validList = [X(valid),Y(valid)];
    if ~isempty(validList)
    	seed = datasample(validList,1,1);
        fail = 0;
    else
        seed = [1,1];
        fail = 1;
    end

end