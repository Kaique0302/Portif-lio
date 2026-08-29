class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method
 

    public   int ExpectedMinutesInOven ()  => 40;
            
    



    // TODO: define the 'RemainingMinutesInOven()' method

    public int RemainingMinutesInOven( int minutes_rest) {

        return ExpectedMinutesInOven() - minutes_rest;
            
        
    }

    // TODO: define the 'PreparationTimeInMinutes()' method


    public int PreparationTimeInMinutes(int calc) {
        
    
        return calc * 2;
    }

    

    // TODO: define the 'ElapsedTimeInMinutes()' method

    public int ElapsedTimeInMinutes(int layers,int RemainingMinutesInOven) {


        
        return PreparationTimeInMinutes(layers) + RemainingMinutesInOven;

        
    }


    
};
