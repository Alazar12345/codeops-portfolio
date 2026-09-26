import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


import Layout from "../components/Layout";

import Home from "../pages/Home";
import Menu from "../pages/Menu";
import DishDetails from "../pages/DishDetails";
import Cart from "../pages/Cart";
import Login from "../pages/Login";
import Checkout from "../pages/Checkout";


function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Layout />}>

          <Route index element={<Home />} />

          <Route 
            path="menu" 
            element={<Menu />} 
          />

          <Route 
            path="dish/:id" 
            element={<DishDetails />} 
          />

          <Route 
            path="cart" 
            element={<Cart />} 
          />

          <Route 
            path="login" 
            element={<Login />} 
          />

          <Route 
            path="checkout" 
            element={<Checkout />} 
          />

        </Route>

      </Routes>

    </BrowserRouter>

  );
}


export default App;