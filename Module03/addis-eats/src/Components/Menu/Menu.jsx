import { useState } from "react";
import Dish from "../Dish/Dish";
import dishes from "../../data";
import "./Menu.css";
import CategoryBar from "../CategoryBar/CategoryBar";


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

      <CategoryBar
    categories={categories}
    selected={category}
    onSelect={setCategory}
/>
      



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