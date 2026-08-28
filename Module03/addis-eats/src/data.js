import shiro from "./assets/shiro.jpg";
import tibs from "./assets/tibs.jpg";
import firfir from "./assets/firfir.jpg";

const dishes = [
  {
    id: 1,
    name: "Shiro",
    price: 120,
    category: "Vegetarian",
    spicy: true,
    image: shiro,
  },
  {
    id: 2,
    name: "Tibs",
    price: 358,
    category: "Meat",
    spicy: true,
    image: tibs,
  },
  {
    id: 3,
    name: "Firfir",
    price: 100,
    category: "Breakfast",
    spicy: false,
    image: firfir,
  },
];

export default dishes;