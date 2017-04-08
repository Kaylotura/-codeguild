import React, { Component, PropTypes } from 'react';

import './App.css';

const JSONInventory = [
  {category: "Sporting Goods", price: "$49.99", stocked: true, name: "Football"},
  {category: "Sporting Goods", price: "$9.99", stocked: true, name: "Baseball"},
  {category: "Sporting Goods", price: "$29.99", stocked: false, name: "Basketball"},
  {category: "Electronics", price: "$99.99", stocked: true, name: "iPod Touch"},
  {category: "Electronics", price: "$399.99", stocked: false, name: "iPhone 5"},
  {category: "Electronics", price: "$199.99", stocked: true, name: "Nexus 7"}
];

class App extends Component {
    constructor() {
        super();
        this.state = {filterStocked: false}
        this.toggleFilterStocked = this.toggleFilterStocked.bind(this)
  }
  toggleFilterStocked() {
        this.setState({filterStocked: !this.state.filterStocked})
  }

  render() {
    return (
        <div>
            <SearchBar
                filterStocked={this.state.filterStocked}
                handleFilterStockedToggle={this.toggleFilterStocked}
            />
            <StockTable inventory={JSONInventory}/>
        </div>
    );
  }
}

class SearchBar extends Component {
    static propTypes = {
       filterStocked: PropTypes.bool,
       handleFilterStockedToggle:PropTypes.func
    }
    render() {
        return (
        <div>
            <input placeholder="Search..." type="text"/>
            <input
                type="checkbox"
                checked={this.props.filterStocked}
                onClick={this.props.handleFilterStockedToggle}
            />
            "Only show products in stock"
        </div>
        )
    }
}

class StockTable extends Component {
    render() {
        let categoryList = [];
        let tablebody = [];
        this.props.inventory.forEach((inventoryItem) => {
            if (categoryList.indexOf(inventoryItem.category) === -1) {
                categoryList.push(inventoryItem.category);
            }
        });

        for (let i = 0; i < categoryList.length; i++) {
            tablebody.push(
                <tr><th colSpan="2">{categoryList[i]}</th></tr>
            );
            this.props.inventory.forEach((inventoryItem) => {
                if (categoryList.indexOf(inventoryItem.category) === i) {
                    if (inventoryItem.stocked) {
                        tablebody.push(
                        <tr>
                            <td>{inventoryItem.name}</td>
                            <td>{inventoryItem.price}</td>
                        </tr>
                        )
                    } else {
                        tablebody.push(
                        <tr>
                            <td style={{color: 'red'}}>{inventoryItem.name}</td>
                            <td>{inventoryItem.price}</td>
                        </tr>
                        )
                    }
                }
            });
        }

        return (
            <table>
                <thead>
                <tr>
                    <strong>
                        <td>Name</td>
                        <td>Price</td>
                    </strong>
                </tr>
                </thead>
                <tbody>
                {tablebody}
                </tbody>
            </table>
         )
    }
}


// Separate out Product Headline
// Separate out Product data line



export default App;
