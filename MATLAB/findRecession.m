function [position, serieVar] = findRecession(serie)
    
    serieVar = (serie(2:end) - serie(1:end-1))./serie(1:end-1);
    recession = 0;
    position = 0;
    for i=2:length(serieVar)
        if ((serieVar(i) < 0) && (serieVar(i - 1) < 0))
            recession(i - 1) = 1;
            recession(i) = 1;
        else
            recession(i) = 0;
        end
    end
    
    recession = [0 recession];
    
    for j=1:length(recession)
        if recession(j) == 1
            position(j) = j;
        end
    end
    position = position(position ~= 0);
    
    
    
end