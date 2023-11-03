package org.velezreyes.quiz.question6;
import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine{

    private static VendingMachineImpl machineInstance;
    private Map<String, DrinkImpl> drinksMap;
    private float balance;
    
    private VendingMachineImpl(){
        drinksMap = new HashMap<>();
        // Add the drinks to the machine
        drinksMap.put("ScottCola", new DrinkImpl("ScottCola", Boolean.TRUE, 0.75f));
        drinksMap.put("KarenTea", new DrinkImpl("KarenTea", Boolean.FALSE, 1f));
        balance = 0f;
    }

    public static VendingMachineImpl getInstance() {
        if (machineInstance == null) {
            machineInstance = new VendingMachineImpl();
        }
        return machineInstance;
    }

    @Override
    public void insertQuarter() {
        this.balance += 0.25f;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        float balanceAfterPayment;
        DrinkImpl deliciosDrink = this.drinksMap.get(name);
        if(deliciosDrink != null){
            balanceAfterPayment = this.balance - deliciosDrink.getPrice();
            if( balanceAfterPayment >= 0f){
                this.balance = balanceAfterPayment;
                return deliciosDrink;
            }else{
                throw new NotEnoughMoneyException();
            }    
        }else{
            throw new UnknownDrinkException();
        }
    }
}
