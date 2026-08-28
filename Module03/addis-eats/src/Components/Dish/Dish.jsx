import PropTypes from "prop-types";
import Card from "../Card/Card";
import "./Dish.css"
import Button from "../Button/Button";
import { useState } from "react";

function Dish({name,price,spicy,currency,image,onAdd}) {
  return (
    <card>
    <div className="dish">
        <img src={image} alt={name} />
      <h2>{name}</h2>

      <p>{price} ETB</p>
      <spicy>🌶️ Spicy</spicy>
    
      <Button text="Add to cart"
      onClick={onAdd}/>
    </div>
    </card>
  );
}

Dish.propTypes = {
name: PropTypes.string.isRequired,
price: PropTypes.number.isRequired,
spicy: PropTypes.bool,
currency: PropTypes.string
};


Dish.defaultProps = {
currency:"ETB",
spicy:false
};


export default Dish;

