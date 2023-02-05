@extends('layouts.app')

@section('content')
    <div class="container">
        <form action="/search" class="row mb-5">
            <div class="col-lg-8 mx-auto">
                <h2 class="font-weight-light mb-4 font-weight-normal">ICGS Portal</h2>
                <div class="bg-white p-5 rounded shadow">
                    <div>
                        <div class="input-group mb-4">
                            <input name="name" type="search" placeholder="Search here..." aria-describedby="button-addon5" class="form-control">
                            <div class="input-group-append">
                                <button id="button-addon5" type="submit" class="btn btn-primary"> <i class="fa fa-search"> </i> </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 mx-auto space bg-white p-5 rounded shadow">

                <div class="row">
                    Age
                    <label class="container1 ml-2">20 - 30
                        <input type="checkbox" name="ages[]" value="20-30">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container1">30 - 40
                        <input type="checkbox" name="ages[]" value="30-40">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container1">40 - 50
                        <input type="checkbox" name="ages[]" value="40-50">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container1">50 - 60
                        <input type="checkbox" name="ages[]" value="50-60">
                        <span class="checkmark"></span>
                    </label>
                    <label class="container1">60 plus
                        <input type="checkbox" name="ages[]" value="60-120">
                        <span class="checkmark"></span>
                    </label>
                </div>
                <div class="mt-1 ml-2">Arrest Date</div>
                <div class="">
                    <input name="arrest_date" value="" data-date-format="dd/mm/yyyy" id="datepicker">
                </div>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.7.1/js/bootstrap-datepicker.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script><script type="text/javascript">
                    $('#datepicker').datepicker({
                        weekStart: 1,
                        daysOfWeekHighlighted: "6,0",
                        autoclose: true,
                        todayHighlight: true,
                    });
                </script>

                <div class="mt-4">
                    <label for="sel1">Gender</label>
                    <select name="gender" class="form-control" id="sel1">
                        <option value="">Select Gender</option>
                        <option value="M">Male</option>
                        <option value="F">Female</option>
                        <option value="O">Other</option>
                    </select>
                </div>
                <div class="mt-4">
                    <label for="sel1">State</label>
                    <select name="state" class="form-control" id="sel1">
                        <option value="">Select State</option>
                        <option value="Karnataka">Karnataka</option>
                        <option value="Kerala">Kerala</option>
                        <option value="Tamil Nadu">Tamil Nadu</option>
                        <option value="Goa">Goa</option>
                    </select>
                </div>
            </div>
        </form>
    </div>
@endsection
