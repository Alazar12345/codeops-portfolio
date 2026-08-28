import PropTypes from "prop-types";
import Card from "../Card/Card";
import "./Dish.css";
import Button from "../Button/Button";


function Dish({name, price, spicy, currency, image, onAdd}) {

  return (
    <Card>

      <div className="dish">

        <img src={image} alt={name} />

        <h2>{name}</h2>

        <p>
          {price} {currency}
        </p>

        {spicy && (
          <span className="spicy">
            🌶️ Spicy
          </span>
        )}

        <Button 
          text="Add to cart"
          onClick={onAdd}
        />

      </div>

    </Card>
  );
}


Dish.propTypes = {
  name: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
  spicy: PropTypes.bool,
  currency: PropTypes.string,
  image: PropTypes.string,
  onAdd: PropTypes.func
};


Dish.defaultProps = {
  currency: "ETB",
  spicy: false
};


export default Dish;