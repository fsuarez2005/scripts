#
# general object functions
#

package Object;

# ===========================================================
# class functions
sub classexists {
	#check if package exists;
	my $class = shift;
	#print $class;
	my %classhash = eval '%'.$class.'::';
	return defined %classhash;
}

sub getclass {
	my $thing = shift;
	return (ref $thing?ref $thing:$thing);
}

sub isclass {
	my $caller = shift;
	return ((! isinstance($caller)) && classexists($caller));
}

sub isinstance {
	my $caller = shift;
	return ! ! ref $caller;
}


#basic constructor
sub new {
	my $class = shift;
	my $self = {@_};
	bless ($self, $class);
	return $self;
}

sub testfunc {
	my $caller = shift;
	print "============================\n";
	if (ref $caller) {
		print "$caller is instance\n";
	}else {
		print "$caller is class\n";
	}
	print "arguments:\n";
	for my $f ( @_ ) {
		print $f."\n";
	}
	print "============================\n";	
}

# ===========================================================
# instance functions

sub displayobj {
	my $self = shift;
	print "$self\n";
	for my $k ( keys %$self ) {
		print "$k => ".$$self{$k}."\n";
	}
}


1;
