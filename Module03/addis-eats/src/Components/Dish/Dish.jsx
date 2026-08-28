
import "./Dish.css"
import Button from "../Button/Button";
import { useState } from "react";

function Dish({name,price,image,onAdd}) {
  return (
    
    <div className="dish">
        <img src={image} alt={name} />
      <h2>{name}</h2>

      <p>{price} ETB</p>
    
      <Button text="Add to cart"
      onClick={onAdd}/>
    </div>
  );
}

export default Dish;

