#!/usr/bin/env ruby

$journal_dir = '/Users/franksuarez/Library/Mobile Documents/com~apple~Pages/Documents/journal'

class JournalEntry
  @@prefix = "journal"

  attr_accessor :year
  attr_accessor :month
  attr_accessor :day

  def initialize(year,month,day)
    @year = year
    @month = month
    @day = day
  end


  def self.filename
   sprintf "%s",@@prefix 
  end

end


class JournalDirectory

end




def journal_year_dir(year)
  sprintf("journal%04d",year)
end

def journal_year_month_dir(year,month)
  sprintf("journal%04d%02d",year,month)
end



def main
  Dir.chdir( $journal_dir )
  p Dir.pwd


  dirs = Dir.glob('**/journal[0-9]*.pages')
  dirs.each {|f| 
    filename_base = File.basename(f)
    p filename_base


  }


end

def test2
  p JournalEntry.filename

end


test2



