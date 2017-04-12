import React, { Component, PropTypes } from 'react';

import './App.css';

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

class SearchBar extends Component {
    static propTypes = {
        filterStocked: PropTypes.bool,
        handleFilterStockedToggle:PropTypes.func,
        searchString: PropTypes.string,
        handleSearchString: PropTypes.func,
    };
    render() {
        return (
        <form>
            <div>
                <input
                    type="text"
                    placeholder="Search..."
                    onChange={ (event) => this.props.handleSearchString(event.target.value)}
                />
            </div>
            <div>
                <input
                    type="checkbox"
                    onClick={this.props.handleFilterStockedToggle}
                />
                "Only show products in stock"
            </div>
        </form>
        )
    }
}

        //Break you Stock Table into children//

class StockTable extends Component {
    static propTypes = {
        filterStocked: PropTypes.bool,
        searchString: PropTypes.string,
        inventory: PropTypes.array,
        priceTotal: PropTypes.number,
        updateInCart: PropTypes.func,
    };
    render() {
        return (
            <table>
                <thead>
                    <tr>

                            <td><strong>Name</strong></td>
                            <td>Price</td>

                    </tr>
                </thead>
                <TableBody
                    inventory={this.props.inventory}
                    filterStocked={this.props.filterStocked}
                    searchString={this.props.searchString}
                    priceTotal={this.props.priceTotal}
                    updateInCart={this.props.updateInCart}
                />
            </table>
         );
    }
}

class TableBody extends Component {
    static propTypes = {
        filterStocked: PropTypes.bool,
        searchString: PropTypes.string,
        inventory: PropTypes.array,
        priceTotal: PropTypes.number,
        updateInCart: PropTypes.func
    };
    constructor() {
        super();
        this.state = {
            rowCheckBoxIs: {},
        };
    }

    render() {
        let categoryList = [];
        let tableBody = [];
        let filteredInventory = this.props.inventory.filter((inventoryItem) => {
            if (inventoryItem.name.toLowerCase().includes(this.props.searchString.toLowerCase()) && !this.props.filterStocked) {
                return inventoryItem
            } else if (inventoryItem.name.toLowerCase().includes(this.props.searchString.toLowerCase()) && this.props.filterStocked && inventoryItem.stocked) {
                return inventoryItem
            }
        });
        filteredInventory.forEach((inventoryItem) => {
            if (categoryList.indexOf(inventoryItem.category) === -1) {
                categoryList.push(inventoryItem.category);
            }
        });
        for (let i = 0; i < categoryList.length; i++) {
            tableBody.push(
                <tr><th colSpan="2">{categoryList[i]}</th></tr>
            );
            filteredInventory.forEach((inventoryItem) => {
                if (categoryList.indexOf(inventoryItem.category) === i) {
                    let styleColor = 'black';
                    if (inventoryItem.stocked) {
                        styleColor = 'black'
                    } else if (!this.props.filterStocked) {
                         styleColor = 'red'
                    }
                    tableBody.push(
                            <tr>
                                <td style={{color: styleColor }}>
                                    <input
                                        type="checkbox"
                                        onChange={
                                            (event) => this.props.updateInCart(inventoryItem.name, inventoryItem.price)
                                        }
                                    />
                                        {inventoryItem.name}
                                </td>
                                <td style={{color: styleColor }}>${inventoryItem.price}</td>
                            </tr>
                    )
                }
            });
        }
        return (
            <tbody>
                {tableBody}
                <tr>
                    <td></td>
                    <td><strong>{this.props.priceTotal}</strong></td>
                </tr>
            </tbody>
        )
    }
}

export default App;