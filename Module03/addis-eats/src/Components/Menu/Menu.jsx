import { useState } from "react";
import Dish from "../Dish/Dish";
import dishes from "../../data";
import "./Menu.css";


function Menu({ addToCart }) {

  const [category, setCategory] = useState("All");


  const categories = [
    "All",
    "Vegetarian",
    "Meat",
    "Breakfast"
  ];


  const filteredDishes =
    category === "All"
      ? dishes
      : dishes.filter(
          (dish) => dish.category === category
        );


  return (
    <section className="menu">


      <h1>
        Addis Eats Menu
      </h1>


      <div className="filters">

        {
          categories.map((cat) => (

            <button
              key={cat}
              onClick={() => setCategory(cat)}
            >
              {cat}
            </button>

          ))
        }

      </div>



      {
        filteredDishes.length === 0 ? (

          <p>
            No dishes found in this category.
          </p>

        ) : (


          <div className="dish-list">

            {
              filteredDishes.map((dish) => (

                <Dish
                  key={dish.id}
                  name={dish.name}
                  price={dish.price}
                  image={dish.image}
                  spicy={dish.spicy}
                  currency="ETB"
                  onAdd={() => addToCart(dish)}
                />

              ))
            }

          </div>


        )
      }


    </section>
  );
}


export default Menu;