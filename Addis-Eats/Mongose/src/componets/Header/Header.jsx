import { useNavigate } from "react-router-dom";

function Header({ cartCount }) {
  const navigate = useNavigate();

  return (
    <header className="header">
      <div className="logo">
        <h1>Mesob House</h1>
        <p>Habesha Restaurant</p>
      </div>

      <nav className="navbar">
        <button onClick={() => navigate("/")}>
          Menu
        </button>

        <button onClick={() => navigate("/cart")}>
          Cart ({cartCount})
        </button>
      </nav>
    </header>
  );
}

export default Header;