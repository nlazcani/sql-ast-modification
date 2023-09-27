import React from 'react';

function ResultDisplay({ data }) {

    return <div>
        {
            Object.keys(data).map((key, _) => (
                <div>
                    <h2>{key.toUpperCase()}</h2>
                    {typeof (data[key]) === 'object'
                        ?
                        <table className="table">
                            <thead>
                            <tr>
                                <th>Column Name</th>
                                <th>Hash</th>
                            </tr>
                            </thead>
                            <tbody>
                            {Object.keys(data[key]).map((item, _) =>
                                <tr>
                                    <th>{item}</th>
                                    <th>{data[key][item]}</th>
                                </tr>
                            )
                            }</tbody></table>
                        : <p style={{ whiteSpace: "pre-wrap" }}>{data[key]}</p>
                    }
                </div>
            ))
        }
    </div>;
}

export default ResultDisplay;