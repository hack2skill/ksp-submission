@extends('layouts.app')

@push('styles')
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
            border-radius:6px;
        }

        th, td {
            text-align: left;
            padding: 8px;
        }

        tr:nth-child(even){background-color: #f2f2f2}

        th {
            background-color: #2c7fea;
            color:white;
        }
    </style>
@endpush

@section('content')
    <div class="container2">
        <table class="rounded shadow">
            <tr>
                <th>State</th>
                <th>District Name</th>
                <th>PS Name</th>
                <th>FIR No</th>
                <th>FIR Date</th>
                <th>Person No</th>
                <th>Arrest Date</th>
                <th>Person Name</th>
                <th>Father Name</th>
                <th>Gender</th>
                <th>AgeWhileOpening</th>
                <th>Age</th>
                <th>Pres Address1</th>
                <th>Perm Address1</th>
                <th>Person Status</th>
                <th>Name</th>
                <th>Major Head</th>
                <th>Minor Head</th>
                <th>Crime No</th>
                <th>Arr ID</th>
                <th>Unit ID</th>
                <th>FIR ID</th>
                <th>DEDT</th>
            </tr>
            @foreach($persons as $person)
                <tr>
                    <td>{{ $person['State'] }}</td>
                    <td>{{ $person['District_Name'] }}</td>
                    <td>{{ $person['PS_Name'] }}</td>
                    <td>{{ $person['FIR_No'] }}</td>
                    <td>{{ $person['FIR_Date'] }}</td>
                    <td>{{ $person['Person_No'] }}</td>
                    <td>{{ $person['Arrest_Date'] }}</td>
                    <td>{{ $person['Person_Name'] }}</td>
                    <td>{{ $person['Father_Name'] }}</td>
                    <td>{{ $person['Gender'] }}</td>
                    <td>{{ $person['AgeWhileOpening'] }}</td>
                    <td>{{ $person['Age'] }}</td>
                    <td>{{ $person['Pres_Address1'] }}</td>
                    <td>{{ $person['Perm_Address1'] }}</td>
                    <td>{{ $person['PersonStatus'] }}</td>
                    <td>{{ $person['Name'] }}</td>
                    <td>{{ $person['Major_Head'] }}</td>
                    <td>{{ $person['Minor_Head'] }}</td>
                    <td>{{ $person['Crime_No'] }}</td>
                    <td>{{ $person['Arr_ID'] }}</td>
                    <td>{{ $person['Unit_ID'] }}</td>
                    <td>{{ $person['FIR_ID'] }}</td>
                    <td>{{ $person['DEDT'] }}</td>
                    <td></td>
                </tr>
            @endforeach
        </table>
    </div>
@endsection
