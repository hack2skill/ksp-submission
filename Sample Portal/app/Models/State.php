<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class State extends Model
{
    protected $table = 'state';

    public static function filter()
    {
        $filter = request()->all();

        $query = self::query();

        if ($filter['name'] ?? false) {
            $query->where('PS_Name', 'like', "%$filter[name]%");
        }

        if ($filter['arrest_date'] ?? false) {
            $query->where('Arrest_Date', "=", $filter['arrest_date']);
        }

        if ($filter['gender'] ?? false) {
            $query->where('Gender', "=", $filter['gender']);
        }

        if (($ages = ($filter['ages'] ?? [])) && is_array($ages) && (count($ages))) {
            $query->where(function ($query) use ($ages) {
                foreach ($ages as $age) {
                    $query->orWhereBetween('Age', explode('-', $age));
                }
            });
        }

        return $query->distinct();
    }
}
