const surname = document.querySelector("[name='surname']");
const name = document.querySelector("[name='name']");

const products = document.querySelectorAll("[name='product']");
const counts = document.querySelectorAll("[type='number']");

const checkout = document.querySelector(".checkout");
const sum = document.querySelector(".sum");

const product_count = {
    "espresso": 0,
    "americano": 0,
    "latte": 0,
    "cappuccino": 0,
    "chocolate_muffin": 0,
    "blueberry_muffin": 0,
    "apple_tart": 0
}

const product_price = {
    "espresso": 0,
    "americano": 0,
    "latte": 0,
    "cappuccino": 0,
    "chocolate_muffin": 0,
    "blueberry_muffin": 0,
    "apple_tart": 0
}

function get_sum() {
    let total = 0;
    for (const product of products)
        total += product_count[product.value] * product_price[product.value];
    return total;
}

products.forEach(product => {
    product.addEventListener("change", function () {
        if (product.checked)
            product_price[product.value] = product.dataset.price;
        else
            product_price[product.value] = 0;
        sum.textContent = `${get_sum()}`;
    })
})

counts.forEach(count => {
    count.addEventListener("change", function () {
        product_count[count.id] = count.value;
        sum.textContent = `${get_sum()}`;
    })
})

checkout.onclick = function () {
    if (surname.value !== "" && name.value !== "")
        alert(`Заказчик: ${surname.value} ${name.value}\n` +
            `Итого: ${sum.textContent} р.`);
    else alert("Укажите фамилию и имя заказчика!");
}