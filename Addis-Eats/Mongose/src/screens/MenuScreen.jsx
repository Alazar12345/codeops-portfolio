import Dishcard from ".././componets/DishCard/DishCard"
function MenuScreen({menu, addToCart}){
    return(
        <div>
            {menu.map((dish) => (<Dishcard
            key={dish.id}
            dish={dish}
            addToCart={addToCart}
            />
            ))}
        </div>
    )
}
export default MenuScreen;