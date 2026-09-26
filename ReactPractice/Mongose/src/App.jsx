import { Routes, Route } from "react-router-dom";
import { lazy, Suspense } from "react";

import "./App.css";

import Header from "./componets/Header/Header";
import Loading from "./componets/Loading/Loading";

import useCartStore from "./store/cartStore";

// Lazy Loaded Pages
const Home = lazy(() => import("./componets/Home/Home"));
const Cart = lazy(() => import("./componets/Cart/cart"));
const DishDetails = lazy(() =>
  import("./componets/pages/DishDetail/DishDetails")
);
const Login = lazy(() => import("./pages/Login/Login"));
const Checkout = lazy(() => import("./pages/Checkout/Checkout"));

function App() {
  const cart = useCartStore((state) => state.cart);

  return (
    <>
      <Header cartCount={cart.length} />

      <Suspense fallback={<Loading />}>
        <Routes>
          <Route path="/" element={<Home />} />

          <Route path="/dish/:id" element={<DishDetails />} />

          <Route path="/cart" element={<Cart />} />

          <Route path="/login" element={<Login />} />

          <Route path="/checkout" element={<Checkout />} />
        </Routes>
      </Suspense>
    </>
  );
}

export default App;