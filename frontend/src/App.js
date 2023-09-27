import React, { useState } from 'react';
import InputForm from './InputForm';
import ResultDisplay from './ResultDisplay';
import './App.css';

function App() {
  const [data, setData] = useState(null);

  const handleMethod = async (sqlQuery, selectedMethod) => {
    try {
      const response = await fetch(`http://localhost:5000/${selectedMethod}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: sqlQuery }),
      });

      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>SQL Query AST Modifier</h1>
      <InputForm onSubmit={handleMethod} />
      {data && (
        <ResultDisplay data={data} />
      )}
    </div>
  );
}

export default App;