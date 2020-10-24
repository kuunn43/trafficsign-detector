clear all;
data = xlsread('exemel.xlsx');
x=1;
for c = 1:100
    gt = data(c,5:8);
    ac = data(c,10:13);
    
    p = gt(3) - gt(1);
    l = gt(4) - gt(2);

    p2 = ac(3) - ac(1);
    l2 = ac(4) - ac(2);
    
    % [xmin ymin]
    A = [gt(1) gt(2) p l];
    B = [ac(1) ac(2) p2 l2];
    
    C = (rectint(A,B));
    total = (p*l) + (p2*l2) - C;
    IoU = C / total;
    
    dataIoU(x).value = IoU;
    x=x+1;
end
% a=struct2table(data);
% 
% writetable(a,'coba.csv');
totalIoU = 0
for i = 1:100
    totalIoU = totalIoU + dataIoU(i).value;
end

finalIoU = totalIoU/100