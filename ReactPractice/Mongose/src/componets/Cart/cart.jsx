import useCartStore from "../../store/cartStore";
function Cart (){
    const {
    cart,
    removeItem,
    increaseQuantity,
    decreaseQuantity
  } = useCartStore();
  const total = cart.reduce(
    (sum, item) =>
      sum + item.price * item.quantity,
    0
  );

if (cart.length === 0) {
  return (
    <div>
      <h2>Your cart is empty</h2>
      <p>Add some dishes from the menu.</p>
    </div>
  );
}
    return(
        <div>
         <h2>
            cart({cart.length})
         </h2>
    
            {cart.map((item) => (
  <div className="cart-items" key={item.id}>
    <h3>{item.name}</h3>

    <p>Price: {item.price} ETB</p>

    <p>Quantity: {item.quantity}</p>
    <button onClick={() => increaseQuantity(item.id)}>+</button>
    <button onClick={() => decreaseQuantity(item.id)}>-</button>
    <button onClick={() => removeItem(item.id)}>Remove</button>
  </div>
))}
           <h2>
             Total: {total} ETB
          </h2>
        </div>
    );
    
}

export default Cart;
