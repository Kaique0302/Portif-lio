static class QuestLogic
{
    public static bool CanFastAttack(bool knightIsAwake)
    {

        
        return knightIsAwake  == !true  ;
    }

    public static bool CanSpy(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake)


        
    {

            return knightIsAwake == true  || archerIsAwake == true  || prisonerIsAwake == true;
        
    }

    public static bool CanSignalPrisoner(bool archerIsAwake, bool prisonerIsAwake)
    {

        return archerIsAwake == false && prisonerIsAwake == true;
    }

    public static bool CanFreePrisoner(bool knightIsAwake, bool archerIsAwake, bool prisonerIsAwake, bool petDogIsPresent)
        
    {


        return archerIsAwake == false  && petDogIsPresent == true || archerIsAwake == false  && knightIsAwake == false  &&  petDogIsPresent == false &&  prisonerIsAwake == true ;

        
    }
}
