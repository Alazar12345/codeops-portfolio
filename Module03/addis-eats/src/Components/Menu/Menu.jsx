import {useState} from "react";
import dishes from "../../data";
import Dish from "../Dish/Dish";


function Menu(){

const [category,setCategory] = useState("All");


const filteredDishes =
category === "All"
?
dishes
:
dishes.filter(
dish=>dish.category === category
);


return(

<section>

<button onClick={()=>setCategory("All")}>
All
</button>


<button onClick={()=>setCategory("Meat")}>
Meat
</button>


<button onClick={()=>setCategory("Vegetarian")}>
Vegetarian
</button>


{
filteredDishes.length === 0 ?

<p>No dishes found.</p>

:

filteredDishes.map(dish=>(

<Dish
key={dish.id}
{...dish}
/>

))

}


</section>

)

}


export default Menu;