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
        this.state = {
            filterStocked: false,
            searchString: ''
        };
        this.toggleFilterStocked = this.toggleFilterStocked.bind(this);
        this.updateSearchString = this.updateSearchString.bind(this)
  }
  toggleFilterStocked() {
        this.setState({filterStocked: !this.state.filterStocked})
  }
  updateSearchString(value) {
        this.setState({searchString: value})
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
        handleSearchString: PropTypes.func
    };
    render() {
        return (
        <div>
            <input
                type="text"
                placeholder="Search..."
                onChange={ (event) => this.props.handleSearchString(event.target.value)}
            />
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
    static propTypes = {
        filterStocked: PropTypes.bool,
        searchString: PropTypes.string,
        inventory: PropTypes.array
    };
    render() {
        let categoryList = [];
        let tableBody = [];
        let filteredInventory = [];

        this.props.inventory.forEach((inventoryItem) => {
            if (inventoryItem.name.toLowerCase().includes(this.props.searchString.toLowerCase()) && !this.props.filterStocked) {

                filteredInventory.push(inventoryItem)
            } else if (inventoryItem.name.toLowerCase().includes(this.props.searchString.toLowerCase()) && this.props.filterStocked && inventoryItem.stocked) {
                filteredInventory.push(inventoryItem)
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
            this.props.inventory.forEach((inventoryItem) => {
                if (categoryList.indexOf(inventoryItem.category) === i) {
                    if (inventoryItem.stocked) {
                        tableBody.push(
                        <tr>
                            <td>{inventoryItem.name}</td>
                            <td>{inventoryItem.price}</td>
                        </tr>
                        )
                    } else if (!this.props.filterStocked) {
                        tableBody.push(
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
                {tableBody}
                </tbody>
            </table>
         )
    }
}


// Separate out Product Headline
// Separate out Product data line



export default App;
