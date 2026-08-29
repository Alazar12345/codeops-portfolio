import "./App.css";
import Header from "./Components/Header/Header";
import Menu from "./Components/Menu/Menu";
import { useState } from "react";
import OrderForm from "./Components/OrderForm/OrderForm";

function App() {

  const [cart, setCart] = useState([]);


  function addToCart(dish) {

    const existing = cart.find(
      (item) => item.id === dish.id
    );


    if (existing) {

      setCart(
        cart.map((item) =>
          item.id === dish.id
            ? {
                ...item,
                qty: item.qty + 1
              }
            : item
        )
      );

    } else {

      setCart([
        ...cart,
        {
          ...dish,
          qty: 1
        }
      ]);

    }

  }


  const total = cart.reduce(
    (sum, item) =>
      sum + item.price * item.qty,
    0
  );


  return (
    <>
      <Header />


      <main>

        <Menu addToCart={addToCart} />


        <section className="cart">

          <h1>
            Cart Items: {cart.length}
          </h1>


          <h2>
            Shopping Cart
          </h2>


          {
            cart.length === 0 ? (

              <p>
                Your cart is empty.
              </p>

            ) : (

              cart.map((item) => (

                <div key={item.id}>

                  <p>
                    {item.name} - {item.qty} x {item.price} ETB
                  </p>

                </div>

              ))

            )
          }
          <OrderForm />

          <h3>
            Total: {total} ETB
          </h3>


        </section>


      </main>

    </>
  );
}


export default App;