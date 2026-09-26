import "./DishCard.css";
import { useNavigate } from "react-router-dom";
import useCartStore from "../../store/cartStore";

function DishCard({ dish }) {

  const navigate = useNavigate();

  const addToCart = useCartStore(
    (state) => state.addToCart
  );


  return (
    <div 
      className="dish-card" 
      onClick={() => navigate(`/dish/${dish.id}`)}
    >

      <div>
        <img 
          src={dish.image}
          alt={dish.name}
        />

        <button className="favorite">
          ♡
        </button>
      </div>


      <div className="dish-content">

        <h3>
          {dish.name}
        </h3>


        <p>
          {dish.description}
        </p>


        <div className="dish-footer">

          <span>
            {dish.price} ETB
          </span>


          <button
            onClick={(e) => {
              e.stopPropagation();
              addToCart(dish);
            }}
            className="add-btn"
          >
            Add
          </button>

        </div>

      </div>

    </div>
  );
}


export default DishCard;