<?php

namespace App\Http\Controllers;

use App\Models\ICJS;

class ICJSController extends Controller
{
    public function search()
    {
        $query = ICJS::filter();

        return view('search', ['persons' => $query->paginate(30)]);
    }
}
