/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package org.velezreyes.quiz.question6;

/**
 *
 * @author oscar
 */
public class DrinkImpl implements Drink{
    
    private String name;
    private Boolean fizzy;
    private float price;
   
    public DrinkImpl(String name, Boolean fizzy, float price){
        this.name = name;
        this.fizzy = fizzy;
        this.price = price;
    }
    
    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public boolean isFizzy() {
        return this.fizzy;
    }
    
    @Override
    public float getPrice() {
        return this.price;
    }
}
