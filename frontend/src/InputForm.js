import React, { useState } from 'react';
import { ApiMethods } from './ApiMethods';

function InputForm({ onSubmit }) {
    const [sqlQuery, setSqlQuery] = useState('');
    const [selectedMethod, setSelectedMethod] = useState(ApiMethods.REBUILD);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit(sqlQuery, selectedMethod);
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea
                value={sqlQuery}
                onChange={(e) => setSqlQuery(e.target.value)}
                placeholder="Enter SQL Query..."
                rows="5"
                cols="40"
            />
            <br />
            <label>
                Command:
                <select value={selectedMethod} onChange={(e) => setSelectedMethod(e.target.value)}>
                <option value={ApiMethods.PARSE}>Parse</option>
                <option value={ApiMethods.MODIFY}>Modify</option>
                <option value={ApiMethods.REBUILD}>Rebuild</option>
                </select>
            </label>
            <button type="submit">Submit</button>
        </form>
    );
}

export default InputForm;