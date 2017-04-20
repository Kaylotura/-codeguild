import React, { Component, PropTypes } from 'react';
import SearchBar from './SearchBar'
import StockTable from './StockTable'
// import './App.css';
// import {mount, shallow, render} from 'enzyme';

const JSONInventory = [
    {category: "Sporting Goods", price: 49.99, stocked: true, name: "Football"},
    {category: "Sporting Goods", price: 9.99, stocked: true, name: "Baseball"},
    {category: "Sporting Goods", price: 29.99, stocked: false, name: "Basketball"},
    {category: "Sporting Goods", price: 29.99, stocked: false, name: "Rock'n'Roll Shin Guards"},
    {category: "Electronics", price: 99.99, stocked: true, name: "iPod Touch"},
    {category: "Electronics", price: 399.99, stocked: false, name: "iPhone 5"},
    {category: "Electronics", price: 199.99, stocked: true, name: "Nexus 7"},
    {category: "Shoes", price: 15.99, stocked: true, name: "Generic FlipFlops"},
    {category: "Shoes", price: 59.99, stocked: false, name: "Adidas Air"},
    {category: "Shoes", price: 79.99, stocked: true, name: "Rock'n'Roll Kicks"},
    {category: "Groceries", price: .99, stocked: true, name: "Navel Orange"},
    {category: "Groceries", price: 1.99, stocked: false, name: "Red Apple"},
    {category: "Groceries", price: 2.99, stocked: true, name: "Rock Candy"},
    {category: "Gifts", price: 129.99, stocked: false, name: "Diamond Ring"},
    {category: "Gifts", price: 19.99, stocked: false, name: "Orange Stuffed Bear"},
    {category: "Gifts", price: 3.99, stocked: false, name: "Flowers for Cuties"},
  ];

class App extends Component {
    constructor() {
        super();
        this.state = {
            filterStocked: false,
            searchString: '',
            inCart: [],
            priceTotal: 0,
        };
        this.toggleFilterStocked = this.toggleFilterStocked.bind(this);
        this.updateSearchString = this.updateSearchString.bind(this);
        this.updateInCart = this.updateInCart.bind(this);
  }
  toggleFilterStocked() {
        this.setState({filterStocked: !this.state.filterStocked})
  }
  updateSearchString(value) {
        this.setState({searchString: value})
  }

  updateInCart(ItemName, ItemPrice) {
        let workingCart = this.state.inCart;
        if (workingCart.indexOf(ItemName) === -1) {
            workingCart.push(ItemName);
            this.setState({priceTotal: this.state.priceTotal + ItemPrice})
        } else {
            let itemNameIndex = workingCart.indexOf(ItemName);
            workingCart.splice(itemNameIndex, 1);
            this.setState({priceTotal: this.state.priceTotal - ItemPrice})
        }
        this.setState({workingCart})
  }

  render() {
    return (
        <div>
            <SearchBar
                filterStocked={this.state.filterStocked}
                handleFilterStockedToggle={this.toggleFilterStocked}
                searchString={this.state.searchString}
                handleSearchString={this.updateSearchString}
            />
            <StockTable
                inventory={JSONInventory}
                filterStocked={this.state.filterStocked}
                searchString={this.state.searchString}
                priceTotal={this.state.priceTotal}
                updateInCart={this.updateInCart}
            />
        </div>
    );
  }
}

export default App;