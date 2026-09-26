import { useParams } from "react-router-dom";
import { useState } from "react";
import dishes from "../../../data/mockData";
import "./DishDetails.css"


function DishDetails({ addToCart }) {

  const { id } = useParams();

  const dish = dishes.find(
    item => item.id === Number(id)
  );


  const [spice, setSpice] = useState("Medium");
  const [injera, setInjera] = useState("Regular");
  const [quantity, setQuantity] = useState(1);


  if (!dish) {
    return <h2>Dish not found</h2>;
  }


  function handleAddToCart(){

    addToCart({
      ...dish,
      spice,
      injera,
      quantity
    });

  }


  return (

    <div className="dish-details">


      <div className="details-image">

        <img
          src={dish.image}
          alt={dish.name}
        />

      </div>



      <div className="details-info">


        <h1>
          {dish.name}
        </h1>


        <p>
          {dish.description}
        </p>


        <h2>
          {dish.price} ETB
        </h2>



        <h3>
          Spice Level
        </h3>


        <div className="options">

          {
            ["Mild","Medium","Hot"].map(level=>(
              <button
                key={level}
                onClick={()=>setSpice(level)}
                className={
                  spice===level
                  ? "selected"
                  :""
                }
              >
                {level}
              </button>
            ))
          }

        </div>



        <h3>
          Injera
        </h3>


        <div className="options">

          {
            ["Regular","Special"].map(type=>(
              <button
                key={type}
                onClick={()=>setInjera(type)}
                className={
                  injera===type
                  ? "selected"
                  :""
                }
              >
                {type}
              </button>
            ))
          }

        </div>



        <div className="quantity">

          <button
          onClick={()=>
            setQuantity(Math.max(1,quantity-1))
          }
          >
            -
          </button>


          <span>
            {quantity}
          </span>


          <button
          onClick={()=>
            setQuantity(quantity+1)
          }
          >
            +
          </button>

        </div>



        <button
        className="add-cart"
        onClick={handleAddToCart}
        >
          Add to Basket
        </button>


      </div>


    </div>

  )

}

export default DishDetails;