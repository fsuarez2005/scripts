# TODO: test module

sub sum_array_slice {
    my $n_array = shift;
    my $index_array = shift;

    my $sum = 0;

    for my $n (@$index_array) {
	
	$sum += $$n_array[$n];
    }

    return $sum;

}


sub sum_odds {
    my @upc = @_;
    my @odds = qw/0 2 4 6 8 10 12/;

    return sum_array_slice(\@upc,\@odds);
}

sub sum_evens {
    my @upc = @_;
    my @evens = qw/1 3 5 7 9/;
    return sum_array_slice(\@upc,\@evens);


}



sub check_upc {
    my $upc_string = shift;
    my @upc = split(//,$upc_string);

    if ((scalar @upc) != 12) {
		return 0;
    }


    my $checksum = 0;

    $checksum += sum_odds(@upc);

    #triple
    $checksum *= 3;

    $checksum += sum_evens(@upc);

    $checksum %= 10;

    if ($checksum != 0) {
		$checksum = 10 - $checksum;
    }



    return($checksum == @upc[11]);
}

