<?php

namespace App\Http\Controllers;

use App\Models\State;
use Illuminate\Http\Request;

class StatesController extends Controller
{
    public function search()
    {
        $query = State::filter();

        return response()->json(['data' => $query->paginate(30)]);
    }
}
