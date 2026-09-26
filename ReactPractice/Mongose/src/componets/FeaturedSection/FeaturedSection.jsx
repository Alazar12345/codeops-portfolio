import dishes from "../../data/mockData"
import DishCard from "../DishCard/DishCard"
import "./FeaturedSection.css"


function FeaturedSection ({addToCart,selectedCategory,searchTerm,}){
    const filteredDishes = dishes.filter((dish) => {
    const matchesCategory =
      selectedCategory === "All" ||
      dish.category === selectedCategory;

    const matchesSearch =
      dish.name
        .toLowerCase()
        .includes(searchTerm.toLowerCase());

    return matchesCategory && matchesSearch;
  });
    return(
        <section>
            <h2>Featured Dishes</h2>
            <div className="featured-container">
                {
                    filteredDishes.map(dish=>(<DishCard
                    key={dish.id}
                    dish={dish}
                    addToCart={addToCart}
                    />))
                }
            </div>
        </section>
    )
}
export default FeaturedSection;
