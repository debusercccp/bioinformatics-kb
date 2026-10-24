function Table(tbl)
  return tbl:walk{Math = function(m)
    if m.mathtype == 'DisplayMath' then return pandoc.Math('InlineMath', m.text) end
  end}
end
