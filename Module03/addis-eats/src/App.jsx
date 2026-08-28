import "./App.css"
import Header from "./Components/Header/Header"
import Dish from "./Components/Dish/Dish"
import shiro from "./assets/shiro.jpg"
import tibs from "./assets/tibs.jpg"
import firfir from "./assets/firfir.jpg"
import {useState} from "react"

const dishes = [
  {id:1,name:"Shiro",price:120,image:shiro,},
  {id:2,name:"Tibs",price:358, image:tibs,},
  {id:3,name:"Firfr",price:100, image:firfir,},
];
function App() {
  
  const [cart,setCart] = useState([]);
  const [total,setTotal] = useState(0)

  


  function addToCart(dish){
 const existing = cart.find(item => item.id === dish.id);

 if(existing){

   setCart(
    cart.map(item =>
      item.id === dish.id
      ? {...item, qty:item.qty + 1}
      : item
    )
   );

 }else{

   setCart([...cart,{...dish, qty:1}]);

 }

     setTotal(total + dish.price)
  
  }
  
 console.log(total)
 
  return (
    <>
      <Header/>
      <main>
        <h1>Cart Items:{cart.lenght}</h1>
        
        
      {dishes.map((dish) => {
        return (
          <Dish
          key={dish.id}
          name={dish.name}
          price={dish.price}
          image={dish.image}
          onAdd={() => addToCart(dish)}
          />
        );
      })}
      <section className="cart">

        <h2>Shopping Cart</h2>

        {cart.length === 0 ? (

            <p>Your cart is empty.</p>

        ) : (

            cart.map((item) => (
                <div key={item.id}>
                    <p>{item.name} - {item.qty} * {item.price}</p>
                    <p> ETB</p>
                    <h3>Total: {total}ETB</h3>
                </div>
          
            ))

        )}

    </section>
      
      </main>
    </>
  );
}

export default App
