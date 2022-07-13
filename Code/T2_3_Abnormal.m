result = [9,length(AbnormalData)];
result_Index = 1;
for i=1:length(AbnormalData)
    i
    i_data = AbnormalData(i,:);
    i_predict = [i_data(1,1); i_data(1,2); i_data(1,3); i_data(1,4)];
    XYZ_predict = sim(Abnormal4D_XYZ_8, i_predict);
%     result(i,1) = XYZ_predict(1);
%     result(i,2) = XYZ_predict(2);
%     result(i,3) = XYZ_predict(3);

    X_predict = XYZ_predict(1);
    Y_predict = XYZ_predict(2);
    Z_predict = XYZ_predict(3);
    
    
    X_de = X_predict - AbnormalXYZ(i,1);
    Y_de = Y_predict - AbnormalXYZ(i,2);   
    Z_de = Z_predict - AbnormalXYZ(i,3);
    
    result(i, 1) = AbnormalXYZ(i,1); 
    result(i, 2) = X_predict;
    result(i, 3) = X_de;
    
        
    result(i, 4) = AbnormalXYZ(i,2);
    result(i, 5) = Y_predict;
    result(i, 6) = Y_de;
    
        
    result(i, 7) = AbnormalXYZ(i,3); 
    result(i, 8) = Z_predict;
    result(i, 9) = Z_de;
end