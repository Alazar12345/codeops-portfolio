// 1. Single State Object (Single source of truth)
const state = {
    products: [],
    cart: [],
    search: "",
};

// DOM Node References
const productsEl = document.querySelector("#menu");
const cartItemsEl = document.querySelector("#cart-items");
const totalEl = document.querySelector("#total"); // Fixed: added missing '#'
const searchEl = document.querySelector("#search");

// 2. Fetching API Data
async function loadProducts() {
    productsEl.textContent = "Loading menu...";
    try {
        const res = await fetch("data/products.json"); // Fixed typo: products.json
        if (!res.ok) throw new Error("HTTP error " + res.status);
        state.products = await res.json();
        render();
    } catch (err) {
        productsEl.textContent = "Could not load the menu.";
    }
}

// 3. Main UI Renderer
function render() {
    const term = state.search.toLowerCase();

    const shownProducts = state.products.filter(product =>
        product.name.toLowerCase().includes(term)
    );

    if (shownProducts.length === 0) {
        productsEl.innerHTML = "<p>No products found matching your search.</p>";
    } else {
        productsEl.innerHTML = shownProducts.map(product => `
            <article class="product" data-id="${product.id}">
                <div>
                    <img src="${product.image}" alt="${product.name}">
                    <span class="category-tag">${product.category}</span>
                    <h3>${product.name}</h3>
                </div>
                <div>
                    <p class="price">${product.price} ETB</p>
                    <button class="add" style="width:100%">Add to Cart</button>
                </div>
            </article>
        `).join("");
    }

    renderCart();
}

// 4. Cart View & Calculation
function renderCart() {
    if (state.cart.length === 0) {
        cartItemsEl.innerHTML = "<li>Your cart is empty.</li>";
    } else {
        cartItemsEl.innerHTML = state.cart.map(item => `
            <li data-id="${item.id}">
                <div>
                    <strong>${item.name}</strong><br>
                    <small>${item.qty} x ${item.price} ETB</small>
                </div>
                <div>
                    <span>${item.price * item.qty} ETB</span>
                    <button class="remove">X</button>
                </div>
            </li>
        `).join("");
    }

    totalEl.textContent = `Total: ${cartTotal()} ETB`;
}

function cartTotal() {
    return state.cart.reduce(
        (sum, item) => sum + item.price * item.qty,
        0
    );
}

// 5. Event Listeners (Delegation & Live Input)
searchEl.addEventListener("input", (e) => {
    state.search = e.target.value;
    render();
});

productsEl.addEventListener("click", (e) => {
    if (!e.target.matches(".add")) return;

    const id = Number(e.target.closest(".product").dataset.id);
    const product = state.products.find(p => p.id === id);
    const line = state.cart.find(item => item.id === id);

    if (line) {
        line.qty++;
    } else {
        state.cart.push({
            ...product,
            qty: 1
        });
    }

    save();
    render();
});

cartItemsEl.addEventListener("click", (e) => {
    if (!e.target.matches(".remove")) return;

    const id = Number(e.target.closest("li").dataset.id);

    state.cart = state.cart.filter(item => item.id !== id);

    save();
    render();
});

// 6. Local Storage Persistence
function save() {
    localStorage.setItem("powerfuel-cart", JSON.stringify(state.cart));
}

function load() {
    const saved = localStorage.getItem("powerfuel-cart");
    if (saved) {
        state.cart = JSON.parse(saved);
    }
}

// 7. Initial Execution Bootstrap
async function init() {
    load();
    await loadProducts();
}

init();