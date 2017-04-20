/**
 * Created by kaylo on 4/19/2017.
 */
import React, { Component, PropTypes } from 'react';


export default class TableBody extends Component {
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
                <tr key={categoryList[i]}><th colSpan="2">{categoryList[i]}</th></tr>
            );
            filteredInventory.forEach((inventoryItem) => {
                if (categoryList.indexOf(inventoryItem.category) === i) {
                    let inventoryId = (inventoryItem.name).replace(/\s+/g, '-').toLowerCase()
                    let styleColor = 'black';
                    if (inventoryItem.stocked) {
                        styleColor = 'black'
                    } else if (!this.props.filterStocked) {
                         styleColor = 'red'
                    }

                    tableBody.push(
                            <tr key={inventoryItem.name}>
                                <td style={{color: styleColor }}>
                                    <input
                                        id={inventoryId}
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
                    <td><strong>Total</strong></td>
                    <td id="priceTotal"><strong>${this.props.priceTotal}</strong></td>
                </tr>
            </tbody>
        )
    }
}